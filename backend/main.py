# main.py
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from rdflib import Graph

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

#get alternateVersions
@app.get("/rdf-character/{file_name}/alternateVersions")
def get_rdf(file_name:str):
    # Replace this with your actual RDF data and SPARQL queries
    g = Graph()
    file_path = f"{file_name}.owl"
    g.parse(file_path)

    query = f"""
    SELECT ?variant ?description
    WHERE {{
        ?variant rdf:type hero:Variant.
        ?variant hero:alternateVersions ?description.
    }}
    """

    results = g.query(query)

    data = {}

    for row in results:
        variant_name = row['variant'].split('#')[1]
        data[variant_name] = row['description']

    return data

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)