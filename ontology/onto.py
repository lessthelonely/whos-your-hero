from owlready import *

onto = get_ontology("http://whosyourhero.com/heroes.owl")

# Entities
class Person(Thing):
    ontology = onto

class Woman(Person):
    ontology = onto

class Man(Person):
    ontology = onto

class NonBinary(Person):
    ontology = onto

class Character(Person):
    ontology = onto

class Trope(Thing):
    ontology = onto

# Properties
class hasAlias(Property):
    ontology = onto
    domain = [Character]
    range = [str]

class birthday(Property):
    ontology = onto
    domain = [Character]
    range = [str]

class characterType(Property):
    ontology = onto
    domain = [Character]
    range = [str]

class appearsIn(Property):
    ontology = onto
    domain = [Character]
    range = [int]

class appearances(Property):
    ontology = onto
    domain = [Character]
    range = [str]

class creation(Property):
    ontology = onto
    domain = [Character]
    range = [str]

class creators(Property):
    ontology = onto
    domain = [Character]
    range = [str]

class deaths(Property):
    ontology = onto
    domain = [Character]
    range = [str]

class disambiguation(Property):
    ontology = onto
    domain = [Character]
    range = [str]

class firstAppearance(Property):
    ontology = onto
    domain = [Character]
    range = [str]

class storyArcs(Property):
    ontology = onto
    domain = [Character]
    range = [str]

class origin(Property):
    ontology = onto
    domain = [Character]
    range = [str]

class otherMedia(Property):
    ontology = onto
    domain = [Character]
    range = [str]

class otherVersion(Property):
    ontology = onto
    domain = [Character]
    range = [str]

class characteristics(Property):
    ontology = onto
    domain = [Character]
    range = [str]

class powers(Property):
    ontology = onto
    domain = [Character]
    range = [str]

class publisher(Property):
    ontology = onto
    domain = [Character]
    range = [str]

class realName(Property):
    ontology = onto
    domain = [Character]
    range = [str]

class summary(Property):
    ontology = onto
    domain = [Character]
    range = [str]

class superName(Property):
    ontology = onto
    domain = [Character]
    range = [str]

class videoGames(Property):
    ontology = onto
    domain = [Character]
    range = [str]

class hasWeaponsEquipment(Property):
    ontology = onto
    domain = [Character]
    range = [str]



class hasTrope(Property):
    ontology = onto
    domain = [Character]
    range = [Trope]

class hasDied(Property):
    ontology = onto
    domain = [Character]
    type = [bool]

class isWoman(Property):
    ontology = onto
    domain = [Character]
    type = [bool]

class isMan(Property):
    ontology = onto
    domain = [Character]
    range = [bool]

class isNonBinary(Property):
    ontology = onto
    domain = [Character]
    range = [bool]


