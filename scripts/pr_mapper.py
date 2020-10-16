#!/usr/bin/env python
#coding: utf-8

from sys import stdin
import json
from random import randint

def fill_graph(graph):
        n = len(graph)
        for u in graph:
                nv = graph[u][1]
                id = graph[u][0]
                vs = []
                for i in range(nv):
                        v = randint(0,n-1)
                        while v == u:
                                v = randint(0,n-1)
                        vs.append(v)
                graph[u] = (id, vs)
        return graph

def read_input(file, graph, separator='\t'):
        for line in file:
                paper = json.loads(line)
                if not paper.has_key('abstract'):
                        continue
                refs = randint(3,12)#len(paper['references'])
                yield (paper['id'], refs)
                graph[i] = (paper['id'], refs)
        graph = fill_graph(graph)

def main(separator='\t'):
        graph = {}
        data = read_input(stdin, graph, separator)
        for paper_id, n_ref in data:
                val = 1.0 / n_ref
                print '%s%s%f' % (paper_id, separator, val)
	for u in graph:
                for v in graph[u][1]:
                        print '%s%s%s' % (graph[u][0], separator, graph[v][0])
        #print graph
if __name__ == "__main__":
        main()

