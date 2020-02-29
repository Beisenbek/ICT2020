from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

doc = {
    'author': 'kimchy2',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
    'gpa': 3.45
}

res = es.index(index="test-index", id=2, body=doc)
print(res['result'])

res = es.get(index="test-index", id=2)
print(res['_source'])

es.indices.refresh(index="test-index")

res = es.search(index="test-index", body={"query": {"match_all": {}}})

print("Got %d Hits:" % res['hits']['total']['value'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])