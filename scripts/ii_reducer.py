#!/usr/bin/env python

from itertools import groupby
from operator import itemgetter
import sys
import re

def read_mapper_output(file, separator='\t'):
	for line in file:
		yield line.rstrip().split(separator, 1)

def main(separator='\t'):
	# index = {}
	data = read_mapper_output(sys.stdin, separator=separator)
	for current_word, group in groupby(data, itemgetter(0)):
		try:
			real_group = [id for _, id in group]
			print "%s%s%s" % (current_word, separator, real_group)
		except ValueError:
			pass

if __name__ == "__main__":
	main()
