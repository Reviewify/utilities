import json, os, operator

directory = 'text_files'

# create new dictionary
words = {}
total_count = 0

for root, _, files in os.walk(directory):
    for f in files:   	
        data = open('text_files/' + f)
        # unncessary because its only one line
        for line in data:
        	obj = json.loads(line)
        	if 'review_id' in obj:
        		review = obj['text']
        		review_words = review.split(' ')
        		for word in review_words:
        			word = word.lower()
        			if word in words:
        				words[word] += 1
        			else:
        				words[word] = 1
        			total_count += 1

print total_count
print(sorted(words.items(), key=operator.itemgetter(1)))