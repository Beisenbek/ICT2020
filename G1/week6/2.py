from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

res = es.search(index="my_index", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total']['value'])
for hit in res['hits']['hits']:
    print(hit["_source"])