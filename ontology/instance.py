from onto import Character, Story, Power
from owlready2 import *
import os

character = Character("Cassandra Cain")
character.isWoman.append(True)


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

def load_appearances(names):
    for folder_name in names:
        f = open(folder_name + "/" + folder_name + "_Character_Appearances.txt", "r")
        for line in f:
            if (line.strip() == ""):
                continue
            character.appearances.append(line.strip())

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

def load_disambiguation(names): #only cassandra has this
    for folder_name in names:
        f = open(folder_name + "/" + folder_name + "_Disambiguation.txt", "r")
        for line in f:
            if (line.strip() == ""):
                continue
            character.disambiguation.append(line.strip())

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
    #TODO: Make a subproperty so we can save names and the descriptions.
    for folder_name in names:
        f = open(folder_name + "/" + folder_name + "_Other_Media.txt", "r")
        for line in f:
            if (line.strip() == ""):
                continue
            character.otherMedia.append(line.strip())

def load_other_version(names):
    for folder_name in names:
        f = open(folder_name + "/" + folder_name + "_Other_Version.txt", "r")
        for line in f:
            if (line.strip() == ""):
                continue
            character.otherVersion.append(line.strip())

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
        f = open(folder_name + "/" + folder_name + "_summary.txt", "r")
        for line in f:
            if (line.strip() == ""):
                continue
            character.summary.append(line.strip())

def load_super_name(names):
    for folder_name in names:
        f = open(folder_name + "/" + folder_name + "_Super Name.txt", "r")
        for line in f:
            if (line.strip() == ""):
                continue
            character.superName.append(line.strip())

def load_trope_names(names):
    #TODO: Make a subproperty so we can save names and the descriptions.
    for folder_name in names:
        f = open(folder_name + "/" + folder_name + "_TropeNames.txt", "r")
        for line in f:
            if (line.strip() == ""):
                continue
            character.hasTrope.append(line.strip())

def load_video_games(names):
    #TODO: Make a subproperty so we can save names and the descriptions.
    for folder_name in names:
        f = open(folder_name + "/" + folder_name + "_Video_Games.txt", "r")
        for line in f:
            if (line.strip() == ""):
                continue
            character.videoGames.append(line.strip())

def load_weapons_and_equipment(names):
    #TODO: Make a subproperty so we can save former and current.
    for folder_name in names:
        f = open(folder_name + "/" + folder_name + "_Weapons_and_Equipment.txt", "r")
        for line in f:
            if (line.strip() == "" or line.strip() == "Current" or line.strip() == "Former"):
                continue
            character.hasWeaponsEquipment.append(line.strip())

load_aliases(["cassandra_cain"])
load_appears_in(["cassandra_cain"])
load_birthday(["cassandra_cain"])
load_character_type(["cassandra_cain"])
load_appearances(["cassandra_cain"])
load_creation(["cassandra_cain"])
load_creators(["cassandra_cain"])
load_deaths(["cassandra_cain"])
load_disambiguation(["cassandra_cain"])
load_first_appearance(["cassandra_cain"])
load_story_arcs(["cassandra_cain"])
load_origin(["cassandra_cain"])
load_other_media(["cassandra_cain"])
load_other_version(["cassandra_cain"])
load_characteristics(["cassandra_cain"])
load_powers_and_abilities(["cassandra_cain"])
load_publisher(["cassandra_cain"])
load_real_name(["cassandra_cain"])
load_summary(["cassandra_cain"])
load_super_name(["cassandra_cain"])
load_trope_names(["cassandra_cain"])
load_video_games(["cassandra_cain"])
load_weapons_and_equipment(["cassandra_cain"])

print(character)

# Save the ontology as an RDF file (including the individual character)
default_world.save(file="cassandra_cain.owl", format="rdfxml")