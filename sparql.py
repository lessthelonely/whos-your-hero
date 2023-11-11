from rdflib import Graph, Namespace

# Load the RDF file
file_path = 'cassandra_cain.owl'
graph = Graph()
graph.parse(file_path)

# Define the namespaces
rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
hero = Namespace("http://whosyourhero.com/heroes.owl#")

# SPARQL query to get the values of alternateVersions
query = """
    SELECT ?character ?alternateVersion
    WHERE {
        ?character hero:alternateVersions ?alternateVersion.
    }
"""

# Execute the query
results = graph.query(query, initNs={"rdf": rdf, "hero": hero})

# Print the results
for row in results:
    character = row.character
    alternate_version = row.alternateVersion
    print(f"Character: {character}, Alternate Version: {alternate_version}")
