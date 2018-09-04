# coding=utf-8
import rdflib
from rdflib import Graph
from rdflib.plugins.sparql import prepareQuery

def readttl(path):
    g = Graph()
    g.parse(path, format='n3')
    name = rdflib.term.Literal(u'TEMP')
    q = prepareQuery(
        'SELECT ?s WHERE { ?s a <http://bigdataocean.eu/bdo/BDOVariable> . ?s <http://purl.org/dc/terms/identifier> ?name . }'
    )

    for row in g.query(q, initBindings={"name": name}):
        print(row.s)

if __name__ == '__main__':
    readttl('/Users/mashenjun/WorkSpace/anapsid/endpoints/db_meta.ttl')
