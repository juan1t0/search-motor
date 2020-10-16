#!/usr/bin/env python
#coding: utf-8

import sys

def read_mapper_output(file, separator='\t'):
        graph, weightsn, weightsc = {}, {}, {}
        for line in file:
                dt = line.rstrip().split(separator, 1)
                try:
                        dt[1] = float(dt[1])
                        weightsn[dt[0]]= 0.0
                        weightsc[dt[0]]= dt[1]
                except:
                        if graph.has_key(dt[0]):
                                graph[dt[0]].append(dt[1])
                        else:
                                graph[dt[0]] = [dt[1]]
        return graph, weightsn, weightsc

def main(separator='\t'):
        for i in range(100):
                graph, currvals, newvals = read_mapper_output(sys.stdin, separator)
                for nid in graph:
                        es = graph[nid]
                        for e in es:
                                try:
                                        newvals[e] += currvals[nid]
                                except:
                                        pass
                for paper_id in newvals:
                        try:
                                w = newvals[paper_id] / float(len(graph[paper_id]))
                        except:
                                w = newvals[paper_id]
                        print '%s%s%f' % (paper_id, separator, w)

                for u in graph :
                        for v in graph[u]:
                                print '%s%s%s' % (u, separator, v)
if __name__ == "__main__":
        main()
