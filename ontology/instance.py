from onto import Character, Story, Power, Trope, Media, Variant
from owlready2 import *
import os

character = Character("Cassandra Cain")
character.isWoman.append(True)
trope = Trope("Abusive Parents")

def load_photos(names):
    for folder_name in names:
        f = open(folder_name + "/" + folder_name + "_Photo.txt", "r")
        for line in f:
            if (line.strip() == ""):
                continue
            character.hasPhoto.append(line.strip())

def load_aliases(names):
    for folder_name in names:
        f = open(folder_name + "/" + folder_name + "_Aliases.txt", "r")
        for line in f:
            if (line.strip() == ""):
                continue
            character.hasAlias.append(line.strip())

def load_appears_in(names):
    for folder_name in names:
        f = open(folder_name + "/" + folder_name + "_Appears in.txt", "r")
        for line in f:
            if (line.strip() == ""):
                continue
            character.appearsIn.append(int(line.strip().split(" ")[0]))

def load_birthday(names):
    for folder_name in names:
        f = open(folder_name + "/" + folder_name + "_Birthday.txt", "r")
        for line in f:
            if (line.strip() == ""):
                continue
            character.birthday.append(line.strip())

def load_character_type(names):
    for folder_name in names:
        f = open(folder_name + "/" + folder_name + "_Character Type.txt", "r")
        for line in f:
            if (line.strip() == ""):
                continue
            character.characterType.append(line.strip())

def load_creation(names):
    for folder_name in names:
        f = open(folder_name + "/" + folder_name + "_Creation.txt", "r")
        for line in f:
            if (line.strip() == ""):
                continue
            character.creation.append(line.strip())

def load_creators(names):
    for folder_name in names:
        f = open(folder_name + "/" + folder_name + "_Creators.txt", "r")
        for line in f:
            if (line.strip() == ""):
                continue
            character.creators.append(line.strip())

def load_deaths(names):
    for folder_name in names:
        f = open(folder_name + "/" + folder_name + "_Died.txt", "r")
        for line in f:
            if (line.strip() == ""):
                continue
            character.deaths.append(line.strip())

def load_first_appearance(names):
    for folder_name in names:
        f = open(folder_name + "/" + folder_name + "_First Appearance.txt", "r")
        for line in f:
            if (line.strip() == ""):
                continue
            character.firstAppearance.append(line.strip())

def load_story_arcs(names):
    for folder_name in names:
        f = open(folder_name + "/" + folder_name + "_Major_Story_Arcs.txt", "r")
        file_contents = [line.strip() for line in f]
        character_story = None 
        for line in range(len(file_contents)):        
            if line % 2 == 0:
                 character_story = Story(file_contents[line].strip())
            else:
                if character_story:
                    character_story.storyDescription.append(file_contents[line].strip())
                    character.storyArcs.append(character_story)

def load_origin(names):
    for folder_name in names:
        f = open(folder_name + "/" + folder_name + "_Origin.txt", "r")
        for line in f:
            if (line.strip() == ""):
                continue
            character.origin.append(line.strip())

def load_other_media(names):
    for folder_name in names:
        f = open(folder_name + "/" + folder_name + "_Other_Media.txt", "r")
        file_contents = [line.strip() for line in f]
        character_media = None
        media_type = ""
        skip_lines = []
        for line in range(len(file_contents)):
            if line in skip_lines:
                continue
            if line == 0:
                character_media = Media(file_contents[line + 1].strip()) # title
                media_type = file_contents[line].strip() # type
                character_media.mediaType.append(media_type) # type
                skip_lines.append(line + 1)
            elif file_contents[line-1].strip() == "": # new type
                character_media = Media(file_contents[line + 1].strip()) # title
                media_type = file_contents[line].strip() # type
                character_media.mediaType.append(media_type)
                skip_lines.append(line + 1)
                # character.otherMedia.append(character_media)
            # titles are on odd lines and descriptions are on even lines
            else:
                if line % 2 != 0: # title
                    character_media = Media(file_contents[line].strip()) # title
                    character_media.mediaType.append(media_type)
                else: # description
                    character_media.mediaDescription.append(file_contents[line].strip())
                    character.otherMedia.append(character_media)

        # for line in f:
        #     if (line.strip() == ""):
        #         continue
        #     character.otherMedia.append(line.strip())

def load_alternate_version(names):
    for folder_name in names:
        f = open(folder_name + "/" + folder_name + "_Alternate_Versions.txt", "r")
        file_contents = [line.strip() for line in f]
        alternate_version = None 
        for line in range(len(file_contents)):        
            if line % 2 == 0:
                 alternate_version = Variant(file_contents[line].strip())
            else:
                if alternate_version:
                    alternate_version.alternateVersions.append(file_contents[line].strip())
                    character.alternateVersions.append(alternate_version)

def load_characteristics(names):
    for folder_name in names:
        f = open(folder_name + "/" + folder_name + "_Personal_Characteristics.txt", "r")
        for line in f:
            if (line.strip() == ""):
                continue
            character.characteristics.append(line.strip())

def load_powers_and_abilities(names):
    for folder_name in names:
        f = open(folder_name + "/" + folder_name + "_Powers_and_Abilities.txt", "r")
        for line in f:
            if (line.strip() == ""):
                continue
            power_info = line.strip().split(":")
            character_power = Power(power_info[0])
            character_power.powerDescription.append(power_info[1])
            character.powers.append(character_power)
        # f = open(folder_name + "/" + folder_name + "_Powers.txt", "r")
        # for line in f:
        #     if (line.strip() == ""):
        #         continue
        #     character.powers.append(line.strip())

def load_publisher(names):
    for folder_name in names:
        f = open(folder_name + "/" + folder_name + "_Publisher.txt", "r")
        for line in f:
            if (line.strip() == ""):
                continue
            character.publisher.append(line.strip())

def load_real_name(names):
    for folder_name in names:
        f = open(folder_name + "/" + folder_name + "_Real Name.txt", "r")
        for line in f:
            if (line.strip() == ""):
                continue
            character.realName.append(line.strip())

def load_summary(names):
    for folder_name in names:
        f = open(folder_name + "/" + folder_name + "_Summary.txt", "r")
        for line in f:
            if (line.strip() == ""):
                continue
            character.summary.append(line.strip())

def load_character_evolution(names):
    for folder_name in names:
        f = open(folder_name + "/" + folder_name + "_Character_Evolution.txt", "r")
        for line in f:
            if (line.strip() == ""):
                continue
            character.evolution.append(line.strip())

def load_super_name(names):
    for folder_name in names:
        f = open(folder_name + "/" + folder_name + "_Super Name.txt", "r")
        for line in f:
            if (line.strip() == ""):
                continue
            character.superName.append(line.strip())

def load_character_tropes(names):
    for folder_name in names:
        f = open(folder_name + "/" + folder_name + "_Tropes.txt", "r", encoding="utf8")
        for line in f:
            if (line.strip() == ""):
                continue
            trope_info = line.strip().split(":")
            character_trope = Trope(trope_info[0])
            character_trope.tropeDescription.append(trope_info[1])
            character.hasTrope.append(character_trope)

def create_character_rdf(character_name, file_name):
    if(character_name == ["cassandra_cain"]):
        character = Character("Cassandra Cain")
        character.isWoman.append(True)
    elif(character_name == ["deadpool"]):
        character = Character("Deadpool")
        character.isMan.append(True)
    elif(character_name == ["emma_frost"]):
        character = Character("Emma Frost")
        character.isWoman.append(True)
    elif(character_name == ["midnighter"]):
        character = Character("Midnighter")
        character.isMan.append(True)
    elif(character_name == ["wally_west"]):
        character = Character("Wally West")
        character.isMan.append(True)

    load_photos(character_name)
    load_aliases(character_name)
    load_alternate_version(character_name)
    load_appears_in(character_name)
    load_birthday(character_name)
    load_character_type(character_name)
    load_creators(character_name)
    load_deaths(character_name)
    load_first_appearance(character_name)
    load_story_arcs(character_name)
    load_origin(character_name)
    load_powers_and_abilities(character_name)
    load_publisher(character_name)
    load_real_name(character_name)
    load_summary(character_name)
    load_super_name(character_name)
    load_character_tropes(character_name)

    if character_name != ["midnighter"]:
        load_other_media(character_name)
        load_characteristics(character_name)

    if character_name != ["wally_west"]:
        load_creation(character_name)
    
    if character_name != ["wally_west"] and character_name != ["cassandra_cain"]:
        load_character_evolution(character_name)


    print(character)
    # Save the ontology as an RDF file (including the individual character)
    default_world.save(file=file_name, format="rdfxml")

    

create_character_rdf(["cassandra_cain"], "cassandra_cain.owl")
create_character_rdf(["deadpool"], "deadpool.owl")
create_character_rdf(["emma_frost"], "emma_frost.owl")
create_character_rdf(["midnighter"], "midnighter.owl")
create_character_rdf(["wally_west"], "wally_west.owl")

"""
def load_tropes(file_name, trope_name):
    f = open("tropes/" + file_name, "r", encoding="utf8")
    trope_description = [line.strip() for line in f]
    trope = Trope(trope_name)
    trope.tropeDescription = trope_description
    print(trope)
    if trope_name == "\"Freaky Friday\" Flip":
        trope_name = "Freaky Friday Flip"
    if trope_name == "\"The Reason You Suck\" Speech":
        trope_name = "The Reason You Suck Speech"
    if trope_name == "\"Well Done, Son\" Guy":
        trope_name = "Well Done Son Guy"
    if trope_name[len(trope_name)-1] == "?":
        trope_name = trope_name[0:len(trope_name)-1]

    rdf_name = trope_name + ".owl"
    default_world.save(file="tropes/" + rdf_name, format="rdfxml")


all_tropes_file = open("all_tropes.txt", "r")
all_tropes = [line.strip() for line in all_tropes_file]
all_tropes.sort()

tropes = []
directory = 'tropes'
for filename in os.scandir(directory):
    if filename.is_file():
        tropes.append(filename.name)
tropes.sort()
# for t in range(len(tropes)):
#     load_tropes(tropes[t], all_tropes[t])

"""


