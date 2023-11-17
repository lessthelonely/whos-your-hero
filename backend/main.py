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

#get photo
@app.get("/rdf-character/{file_name}/photo")
def get_photo(file_name:str):
    g = Graph()
    file_path = f"{file_name}.owl"
    g.parse(file_path)

    query = f"""
    SELECT ?individual ?photo
    WHERE {{
        ?individual hero:hasPhoto ?photo.
    }}
    """

    results = g.query(query)

    data = {}

    for row in results:
        individual_uri, photo = row
        data.setdefault(str(individual_uri), []).append(str(photo))

    return data

#get birthday
@app.get("/rdf-character/{file_name}/birthday")
def get_birthday(file_name:str):
    g = Graph()
    file_path = f"{file_name}.owl"
    g.parse(file_path)

    query = f"""
    SELECT ?individual ?birthday
    WHERE {{
        ?individual hero:birthday ?birthday.
    }}
    """

    results = g.query(query)

    data = {}

    for row in results:
        individual_uri, birthday = row
        data.setdefault(str(individual_uri), []).append(str(birthday))

    return data

#get characterType
@app.get("/rdf-character/{file_name}/characterType")
def get_characterType(file_name:str):
    g = Graph()
    file_path = f"{file_name}.owl"
    g.parse(file_path)

    query = f"""
    SELECT ?individual ?characterType
    WHERE {{
        ?individual hero:characterType ?characterType.
    }}
    """

    results = g.query(query)

    data = {}

    for row in results:
        individual_uri, characterType = row
        data.setdefault(str(individual_uri), []).append(str(characterType))

    return data

#get number of issues the character appears in
@app.get("/rdf-character/{file_name}/appearsIn")
def get_appearsIn(file_name:str):
    g = Graph()
    file_path = f"{file_name}.owl"
    g.parse(file_path)

    query = f"""
    SELECT ?individual ?appearsIn
    WHERE {{
        ?individual hero:appearsIn ?appearsIn.
    }}
    """

    results = g.query(query)

    data = {}

    for row in results:
        individual_uri, appearsIn = row
        data.setdefault(str(individual_uri), []).append(str(appearsIn))

    return data

#get evolution
@app.get("/rdf-character/{file_name}/evolution")
def get_evolution(file_name:str):
    g = Graph()
    file_path = f"{file_name}.owl"
    g.parse(file_path)
    query = f"""
    SELECT ?individual ?evolution
    WHERE {{
        ?individual hero:evolution ?evolution.
    }}
    """

    results = g.query(query)

    data = {}

    for row in results:
        individual_uri, evolution = row
        data.setdefault(str(individual_uri), []).append(str(evolution))

    return data

#get creation
@app.get("/rdf-character/{file_name}/creation")
def get_creation(file_name:str):
    g = Graph()
    file_path = f"{file_name}.owl"

    g.parse(file_path)

    query = f"""
    SELECT ?individual ?creation
    WHERE {{
        ?individual hero:creation ?creation.
    }}
    """

    results = g.query(query)

    data = {}

    for row in results:
        individual_uri, creation = row
        data.setdefault(str(individual_uri), []).append(str(creation))

    return data

#get creators
@app.get("/rdf-character/{file_name}/creators")
def get_creators(file_name:str):
    g = Graph()
    file_path = f"{file_name}.owl"

    g.parse(file_path)

    query = f"""
    SELECT ?individual ?creators
    WHERE {{
        ?individual hero:creators ?creators.
    }}
    """

    results = g.query(query)

    data = {}

    for row in results:
        individual_uri, creators = row
        data.setdefault(str(individual_uri), []).append(str(creators))

    return data

#get deaths
@app.get("/rdf-character/{file_name}/deaths")
def get_deaths(file_name:str):
    g = Graph()
    file_path = f"{file_name}.owl"

    g.parse(file_path)

    query = f"""
    SELECT ?individual ?deaths
    WHERE {{
        ?individual hero:deaths ?deaths.
    }}
    """

    results = g.query(query)

    data = {}

    for row in results:
        individual_uri, deaths = row
        data.setdefault(str(individual_uri), []).append(str(deaths))

    return data

#get origins
@app.get("/rdf-character/{file_name}/origins")
def get_origins(file_name:str):
    g = Graph()
    file_path = f"{file_name}.owl"

    g.parse(file_path)

    query = f"""
    SELECT ?individual ?origins
    WHERE {{
        ?individual hero:origins ?origins.
    }}
    """

    results = g.query(query)

    data = {}

    for row in results:
        individual_uri, origins = row
        data.setdefault(str(individual_uri), []).append(str(origins))

    return data

#get characteristics
@app.get("/rdf-character/{file_name}/characteristics")
def get_characteristics(file_name:str):
    g = Graph()
    file_path = f"{file_name}.owl"

    g.parse(file_path)

    query = f"""
    SELECT ?individual ?characteristics
    WHERE {{
        ?individual hero:characteristics ?characteristics.
    }}
    """

    results = g.query(query)

    data = {}

    for row in results:
        individual_uri, characteristics = row
        data.setdefault(str(individual_uri), []).append(str(characteristics))

    return data

#get publisher
@app.get("/rdf-character/{file_name}/publisher")
def get_publisher(file_name:str):
    g = Graph()
    file_path = f"{file_name}.owl"

    g.parse(file_path)

    query = f"""
    SELECT ?individual ?publisher
    WHERE {{
        ?individual hero:publisher ?publisher.
    }}
    """

    results = g.query(query)

    data = {}

    for row in results:
        individual_uri, publisher = row
        data.setdefault(str(individual_uri), []).append(str(publisher))

    return data

#get realName
@app.get("/rdf-character/{file_name}/realName")
def get_realName(file_name:str):
    g = Graph()
    file_path = f"{file_name}.owl"

    g.parse(file_path)

    query = f"""
    SELECT ?individual ?realName
    WHERE {{
        ?individual hero:realName ?realName.
    }}
    """

    results = g.query(query)

    data = {}

    for row in results:
        individual_uri, realName = row
        data.setdefault(str(individual_uri), []).append(str(realName))

    return data

#get summary
@app.get("/rdf-character/{file_name}/summary")
def get_summary(file_name:str):
    g = Graph()
    file_path = f"{file_name}.owl"

    g.parse(file_path)

    query = f"""
    SELECT ?individual ?summary
    WHERE {{
        ?individual hero:summary ?summary.
    }}
    """

    results = g.query(query)

    data = {}

    for row in results:
        individual_uri, summary = row
        data.setdefault(str(individual_uri), []).append(str(summary))

    return data

#get superName
@app.get("/rdf-character/{file_name}/superName")
def get_superName(file_name:str):
    g = Graph()
    file_path = f"{file_name}.owl"

    g.parse(file_path)

    query = f"""
    SELECT ?individual ?superName
    WHERE {{
        ?individual hero:superName ?superName.
    }}
    """

    results = g.query(query)

    data = {}

    for row in results:
        individual_uri, superName = row
        data.setdefault(str(individual_uri), []).append(str(superName))

    return data

#get hasDied -> not really needed because we have deaths: if a character hasn't died, deaths will return None
@app.get("/rdf-character/{file_name}/hasDied")
def get_hasDied(file_name:str):
    g = Graph()
    file_path = f"{file_name}.owl"

    g.parse(file_path)

    query = f"""
    SELECT ?individual ?hasDied
    WHERE {{
        ?individual hero:hasDied ?hasDied.
    }}
    """

    results = g.query(query)

    data = {}

    for row in results:
        individual_uri, hasDied = row
        data.setdefault(str(individual_uri), []).append(str(hasDied))

    return data

#get isWoman
@app.get("/rdf-character/{file_name}/isWoman")
def get_isWoman(file_name:str):
    g = Graph()
    file_path = f"{file_name}.owl"

    g.parse(file_path)

    query = f"""
    SELECT DISTINCT ?individual ?isWoman
    WHERE {{
        ?individual hero:isWoman ?isWoman.
    }}
    """

    results = g.query(query)

    data = {}

    for row in results:
        individual_uri, isWoman = row
        data.setdefault(str(individual_uri), []).append(str(isWoman))

    return data

#get isMan
@app.get("/rdf-character/{file_name}/isMan")
def get_isMan(file_name:str):
    g = Graph()
    file_path = f"{file_name}.owl"

    g.parse(file_path)

    query = f"""
    SELECT DISTINCT ?individual ?isMan
    WHERE {{
        ?individual hero:isMan ?isMan.
    }}
    """

    results = g.query(query)

    data = {}

    for row in results:
        individual_uri, isMan = row
        data.setdefault(str(individual_uri), []).append(str(isMan))

    return data

#get isNonBinary
@app.get("/rdf-character/{file_name}/isNonBinary")
def get_isNonBinary(file_name:str):
    g = Graph()
    file_path = f"{file_name}.owl"

    g.parse(file_path)

    query = f"""
    SELECT DISTINCT ?individual ?isNonBinary
    WHERE {{
        ?individual hero:isNonBinary ?isNonBinary.
    }}
    """

    results = g.query(query)

    data = {}

    for row in results:
        individual_uri, isNonBinary = row
        data.setdefault(str(individual_uri), []).append(str(isNonBinary))

    return data

#get firstAppearance
@app.get("/rdf-character/{file_name}/firstAppearance")
def get_firstAppearance(file_name:str):
    g = Graph()
    file_path = f"{file_name}.owl"

    g.parse(file_path)

    query = f"""
    SELECT ?individual ?firstAppearance
    WHERE {{
        ?individual hero:firstAppearance ?firstAppearance.
    }}
    """

    results = g.query(query)

    data = {}

    for row in results:
        individual_uri, firstAppearance = row
        data.setdefault(str(individual_uri), []).append(str(firstAppearance))

    return data

#get alias
@app.get("/rdf-character/{file_name}/alias")
def get_alias(file_name:str):
    g = Graph()
    file_path = f"{file_name}.owl"
    g.parse(file_path)

    query = f"""
    SELECT ?individual ?alias
    WHERE {{
        ?individual hero:hasAlias ?alias.
    }}
    """

    results = g.query(query)

    data = {}

    for row in results:
        individual_uri, alias = row
        data.setdefault(str(individual_uri), []).append(str(alias))

    return data

#get alternateVersions
@app.get("/rdf-character/{file_name}/alternateVersions")
def get_alternateVersions(file_name:str):
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
def get_storyArcs(file_name:str):
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
def get_powers(file_name:str):
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

def trope_query(file_path):
    g = Graph()
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


#get character's tropes
@app.get("/rdf-character/{file_name}/tropes")
def get_character_tropes(file_name:str):
    file_path = f"{file_name}.owl"
   
    return trope_query(file_path)

#get Trope's information
@app.get("/rdf-trope/{file_name}")
def get_trope(file_name:str):
    file_path = "./tropes/owls/" + file_name + ".owl"
   
    return trope_query(file_path)

#get media
@app.get("/rdf-character/{file_name}/media")
def get_media(file_name:str):
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


#get shared values of a trope that various characters might have
@app.get("/rdf-all/trope/{trope_name}")
def get_trope_descriptions(trope_name: str):
    g = Graph()
    file_path = "output.owl"
    g.parse(file_path)

    query = f"""
        SELECT ?belongsTo ?tropeDescription
        WHERE {{
            ?trope rdf:type hero:Trope.
            ?trope hero:belongsTo ?belongsTo.
            ?trope hero:tropeDescription ?tropeDescription.
            FILTER (?trope = hero:{trope_name})
        }}
    """

    results = list(g.query(query))
    data = {}

    if len(results) > 0:
        belongsTo_list = [row.belongsTo.toPython().split('#')[1] for row in results]
        tropeDescription_list = [row.tropeDescription.toPython() for row in results]

        offset = 0
        for i in range(len(belongsTo_list)):
            if belongsTo_list[i] in data:
                offset += 1
                continue

            data[belongsTo_list[i]] = tropeDescription_list[i - offset]

    return data


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)