from rdflib import Graph

# Create a new RDF graph (store)
rdf_store = Graph()

# Load data from your RDF files into the RDF graph
rdf_store.parse("cassandra_cain.owl", format="xml")
rdf_store.parse("wally_west.owl", format="xml")
rdf_store.parse("deadpool.owl", format="xml")
rdf_store.parse("emma_frost.owl", format="xml")
rdf_store.parse("midnighter.owl", format="xml")

# You now have all the data from the RDF files in the rdf_store

# Example: Print the number of triples in the RDF store
print(f"Number of triples in the RDF store: {len(rdf_store)}")
# Save the RDF store to a file (e.g., output.rdf)
rdf_store.serialize("output.owl", format="xml")