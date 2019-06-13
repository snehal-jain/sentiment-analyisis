import os

from os import listdir

def load_doc(filename):
	# open the file as read only
	file = open(filename, 'r')
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text
 
# specify directory to load
directory = 'Desktop/txt_sentoken/neg'
# walk through all files in the folder
for filename in listdir(directory):
	# skip files that do not have the right extension
	if not filename.endswith(".txt"):
		continue
	# create the full path of the file to open
	path = directory + '/' + filename
	# load document
	doc = load_doc(path)
	print('Loaded %s' % filename)

directory = 'Desktop/txt_sentoken/neg'
process_docs(directory)
def load_doc(filename):
	# open the file as read only
	file = open(filename, 'r')
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text
filename = 'Desktop/txt_sentoken/neg/cv258_5627.txt'
text = load_doc(filename)
# split into tokens by white space
tokens = text.split()
print(tokens)
