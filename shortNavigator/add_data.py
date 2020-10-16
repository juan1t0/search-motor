# paper
from polls.models import Paper

import sys
import json
import os

ranks = {}
rfiles = ['part-00000','part-00001']#os.listdir('./data/pagerank')
for rf in rfiles:
  with open('./data/pagerank/'+ rf, 'r') as file_ranks:
    for line in file_ranks:
      r = line.rstrip().split('\t')
      # print(r[0],float(r[1]))
      # break
      ranks[r[0]] = float(r[1])

print(len(ranks))
c1,c2,c3 = 0,0,0

with open('./data/dblp-ref-3.json','r') as file_json:
	for line in file_json:
		paper = json.loads(line)
		if 'abstract' in paper:
			cid = paper['id']
			if cid in ranks:
				p = Paper(paper_id=paper['id'],abstract=paper['abstract'],title=paper['title'])
				p.rank=ranks[paper['id']]
				if 'year' in paper:
					p.year = paper['year']
				else:
					p.year = '0000'
				if 'authors' in paper:
					p.authors = paper['authors'],
				else:
					p.authors = 'None'
				p.save()
    
    # print(p)
    # del paper
    # break

print(c1,c2,c3)
print(Paper.objects.all().count())

## words

##insertar solo part 00 y 04
'''
subir todos los papers, no solo 10
poner boton de home
'''


from polls.models import Word, Paper
import sys
import os
#ivfiles = os.listdir('./data/invidx03')
#digs = ['0','1','2','3','4','5','6','7','8','9','_']
c1,c2=0,0
#for ivf in ivfiles:
#with open('./data/invidx03/'+ivf, 'r') as file_inv:
file_inv = open('./data/invidx/part-00002')
for i,line in enumerate(file_inv):
	r = line.rstrip().split('\t')
	idxs = r[1].split(';')
	for id in idxs:
		try:
			paper = Paper.objects.get(paper_id=id)
			w = Word(word=r[0],origin=paper)
			w.save()
		except:
			pass
	if (i+1)%1000 == 0:
		print ('van',i+1,'words')

print(Word.objects.all().count())