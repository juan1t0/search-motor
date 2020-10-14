#!/usr/bin/env python
from sys import stdin
import re
import os
import json
#import string

#from nltk.corpus import stopwords

stop_words= ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 
	'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 
	'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 
	'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 
	'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 
	'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 
	'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 
	'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 
	'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 
	'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 
	'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 
	'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 
	'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 
	'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 
	'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 
	'here', 'than']

def read_input(file):
	for line in file:
		paper = json.loads(line)
		# for i,paper in enumerate(data):
		if not paper.has_key('abstract'):
			continue
		text = re.sub(r'[^\w\s]', '', (paper['abstract'] + ' ' + paper['title'])).lower().split()
		text = [w for w in text if not w in stop_words]
		yield (paper['id'], text)

def main(separator='\t'):
	data = read_input(stdin)

	for paper_id, words in data:
		for word in words:
			print '%s%s%s' % (word, separator, paper_id)

if __name__ == "__main__":
	main()
