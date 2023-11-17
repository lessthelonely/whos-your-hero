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

#get storyArcs
@app.get("/rdf-character/{file_name}/storyArcs")
def get_rdf(file_name:str):
    # Replace this with your actual RDF data and SPARQL queries
    g = Graph()
    file_path = f"{file_name}.owl"
    g.parse(file_path)

    query = f"""
    SELECT ?story ?description
    WHERE {{
        ?story rdf:type hero:Story.
        ?story hero:storyDescription ?description.
    }}
    """

    results = g.query(query)

    data = {}

    for row in results:
        story_name = row['story'].split('#')[1]
        data[story_name] = row['description']

    return data

#get powers
@app.get("/rdf-character/{file_name}/powers")
def get_rdf(file_name:str):
    # Replace this with your actual RDF data and SPARQL queries
    g = Graph()
    file_path = f"{file_name}.owl"
    g.parse(file_path)

    query = f"""
    SELECT ?power ?description
    WHERE {{
        ?power rdf:type hero:Power.
        ?power hero:powerDescription ?description.
    }}
    """

    results = g.query(query)

    data = {}

    for row in results:
        power_name = row['power'].split('#')[1]
        data[power_name] = row['description']

    return data

#get character's tropes
@app.get("/rdf-character/{file_name}/tropes")
def get_rdf(file_name:str):
    # Replace this with your actual RDF data and SPARQL queries
    g = Graph()
    file_path = f"{file_name}.owl"
    g.parse(file_path)

    query = f"""
    SELECT ?trope ?description
    WHERE {{
        ?trope rdf:type hero:Trope.
        ?trope hero:tropeDescription ?description.
    }}
    """

    results = g.query(query)

    data = {}

    for row in results:
        trope_name = row['trope'].split('#')[1]
        data[trope_name] = row['description']

    return data

#get media
@app.get("/rdf-character/{file_name}/media")
def get_rdf(file_name:str):
    # Replace this with your actual RDF data and SPARQL queries
    g = Graph()
    file_path = f"{file_name}.owl"
    g.parse(file_path)

    query = f"""
    SELECT ?media ?type ?description
    WHERE {{
        ?media rdf:type hero:Media.
        OPTIONAL {{ ?media hero:mediaType ?type. }}
        OPTIONAL {{ ?media hero:mediaDescription ?description. }}
    }}

    """

    results = g.query(query)

    data = {}

    for row in results:
        media = row.media.split('#')[1]
        media_type = row.type
        media_description = row.description

        data[media] = {
            "mediaType": media_type,
            "mediaDescription": media_description,
        }

    return data


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)