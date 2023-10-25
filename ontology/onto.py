from owlready import *
import datetime

onto = get_ontology("http://whosyourhero.com/heroes.owl")

# Entities
class Person(Thing):
    ontology = onto

class Woman(Person):
    ontology = onto

class Man(Person):
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

class Birthday(Property):
    ontology = onto
    domain = [Character]
    range = [datetime]

class CharacterType(Property):
    ontology = onto
    domain = [Character]
    range = [str]

class Appearances(Property):
    ontology = onto
    domain = [Character]
    range = [str]

class Deaths(Property):
    ontology = onto
    domain = [Character]
    range = [str]

class StoryArcs(Property):
    ontology = onto
    domain = [Character]
    range = [str]

class Origin(Property):
    ontology = onto
    domain = [Character]
    range = [str]

class OtherMedia(Property):
    ontology = onto
    domain = [Character]
    range = [str]

class OtherVersion(Property):
    ontology = onto
    domain = [Character]
    range = [str]

class Characteristics(Property):
    ontology = onto
    domain = [Character]
    range = [str]

class Powers(Property):
    ontology = onto
    domain = [Character]
    range = [str]

class Publisher(Property):
    ontology = onto
    domain = [Character]
    range = [str]

class RealName(Property):
    ontology = onto
    domain = [Character]
    range = [str]

class Summary(Property):
    ontology = onto
    domain = [Character]
    range = [str]

class SuperName(Property):
    ontology = onto
    domain = [Character]
    range = [str]

class TropeNames(Property):
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


