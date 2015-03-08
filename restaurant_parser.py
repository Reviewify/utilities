# This script separates reviews into directories corresponding to the
# business_id listed in the review

import json, os, errno
from shutil import copyfile


def make_directory(path, directory):
	if not os.path.exists(path + directory):
		os.makedirs(path + directory)

def get_restaurant_name(path, file_name):
	# opens a file as a JSON object
	obj = json.loads(open(os.path.join(path, file_name)).readline())
	return obj['name']

def main():
	path = 'test_files/restaurant/'
	for root, _, files in os.walk(path):
		for f in files:
			name = get_restaurant_name(path, f)
			make_directory(path, name)
			# copies file into appropriate business directory
			copyfile(os.path.join(path, f), os.path.join(path, name, f))

main()