#!/usr/bin/env python
#coding: utf-8

from sys import stdin
import json

def read_input(file, separator='\t'):
	for line in file:
                paper = json.loads(line)
                if not paper.has_key('abstract'):
			continue
		if not paper.has_key('references'):
			yield (paper['id'], 0.0)
                refs = paper['references']
                yield (paper['id'], float(len(refs))
                for r in refs:
                        yield (paper['id'], r)

def main(separator='\t'):
	data = read_input(stdin, separator)
	for paper_id, n_ref in data:
		if type(n_ref) is not float:
			print '%s%s%s' % (paper_id, separator, n_ref)
			continue
		if n_ref == 0.0:
			val = 1.0
		else:
			val = 1.0 / n_ref
		print '%s%s%f' % (paper_id, separator, val)

if __name__ == "__main__":
	main()
