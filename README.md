# Motor de Busquedad

## Dataset
- https://www.kaggle.com/kmader/aminer-academic-citation-dataset

## Ejecución en google cloud
- Indice invertido

`hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -file ./scripts/ii_mapper.py -mapper ./scripts/ii_mapper.py -file ./scripts/ii_reducer.py -reducer ./scripts/ii_reducer.py -input /aminer/*.json -output /invidx
`

- PageRank

`hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -file ./scripts/pr_mapper.py -mapper ./scripts/pr_mapper.py -file ./scripts/pr_reducer.py -reducer ./scripts/pr_reducer.py -input /aminer/*.json -output /pagerank0
`

`hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -mapper '/usr/bin/cat' -file ./scripts/pr_reducer2.py -reducer ./scripts/pr_reducer2.py -input /pagerank0/part* -output /pagerank
`

## Aplicación Web
Realizada con `django`
