import json, os, operator, pickle, re
from pattern.en import pluralize, singularize, suggest

# open stopword list
stopwords = pickle.load(open("stopwords/stopwords.pickle", "rb"))

def singularize_words(words_list):
	return map(singularize, words_list)

def lowercase_words(words_list):
	return map(lambda x: x.lower(), words_list)

def correct_words(words_list):
	return [tup[0][0] for tup in map(suggest, words_list)]

def word_in_stopwords(word):
	return word not in stopwords

def remove_stop_words(words_list):
	return filter(word_in_stopwords, words_list)

def clean_words_list(words_list):
	return remove_stop_words(correct_words(lowercase_words(singularize_words(words_list))))


def main():
	directory = 'test_files'
	# create new dictionary
	words = {}
	total_count = 0
	clean_words = set()

	for root, _, files in os.walk(directory):
	    for f in files:   	
	        data = open('text_files/' + f)
	        # unncessary because its only one line
	        for line in data:
	        	obj = json.loads(line)
	        	if 'review_id' in obj:
	        		review = obj['text']
	        		review_words = re.split('\W+', review)
	        		clean_words = clean_words_list(review_words)
	        		for word in clean_words:
	    				if word in words and word:
	    					words[word] += 1
	    				else:
	    					words[word] = 1
	    					total_count += 1
	        			

	print total_count
	print(sorted(words.items(), key=operator.itemgetter(1)))

if __name__ == "__main__": main()