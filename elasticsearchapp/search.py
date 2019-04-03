from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models

connections.create_connection()

class UsuarioIndex(DocType):
    usuario = Text()
    bio = Text()
    web = Text()

    class Meta:
        index = 'user-index'

def bulk_indexing():
    UsuarioIndex.init(index='user-index')
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in models.Perfil.objects.all().iterator()))
