# Utility script to parse the dataset provided by Yelp, generating an individual text
# file for each JSON object. Differentiates between User, Review, and Business objects.

# Run in the directory that contains the JSON file(s)

import json
from pprint import pprint

data = open('yelp_small.json')
for line in data:
	obj = json.loads(line)
	if 'votes' in obj:
		print obj['votes']['funny']

data.close()