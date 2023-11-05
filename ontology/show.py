from pronto import Ontology

ont = Ontology('../cassandra_cain.owl')

ont.show(ont['hasDied'])