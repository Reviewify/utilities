# Utility script to parse the dataset provided by Yelp, generating an individual text
# file for each JSON object. Differentiates between User, Review, and Business objects.

# Run in the directory that contains the JSON file(s)

import json, os
from pprint import pprint

data = open('yelp_small.json')
for line in data:
	obj = json.loads(line)
	# user object
	if 'name' in obj and 'user_id' in obj:
		file_name = 'user-' + obj['user_id']
	# review object
	elif 'review_id' in obj:
		file_name = 'review-' + obj['review_id']
	# restaurant object
	else:
		file_name = 'restaurant-' + obj['business_id']

	f = open(os.path.join('text_files', file_name), 'w')
	f.write(line)
	f.close()

data.close()