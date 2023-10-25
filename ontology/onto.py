from owlready2 import *

# Create and load your ontology
onto = get_ontology("http://whosyourhero.com/heroes.owl")

# Entities
with onto:
    class Person(Thing):
        pass

    class Woman(Person):
        pass

    class Man(Person):
        pass

    class NonBinary(Person):
        pass

    class Character(Person):
        pass

    class Trope(Thing):
        pass

    # Define the Story class
    class Story(Thing):
        pass

# Properties
with onto:
    class storyDescription(Property):
        domain = [Story]
        range = [str]

    class hasAlias(Property):
        domain = [Character]
        range = [str]

    class birthday(Property):
        domain = [Character]
        range = [str]

    class characterType(Property):
        domain = [Character]
        range = [str]

    class appearsIn(Property):
        domain = [Character]
        range = [int]

    class appearances(Property):
        domain = [Character]
        range = [str]

    class creation(Property):
        domain = [Character]
        range = [str]

    class creators(Property):
        domain = [Character]
        range = [str]

    class deaths(Property):
        domain = [Character]
        range = [str]

    class disambiguation(Property):
        domain = [Character]
        range = [str]

    class firstAppearance(Property):
        domain = [Character]
        range = [str]

    # Define the storyArcs property
    class storyArcs(Property):
        domain = [Character]
        range = [Story]

    class origin(Property):
        domain = [Character]
        range = [str]

    class otherMedia(Property):
        domain = [Character]
        range = [str]

    class otherVersion(Property):
        domain = [Character]
        range = [str]

    class characteristics(Property):
        domain = [Character]
        range = [str]

    class powers(Property):
        domain = [Character]
        range = [str]

    class publisher(Property):
        domain = [Character]
        range = [str]

    class realName(Property):
        domain = [Character]
        range = [str]

    class summary(Property):
        domain = [Character]
        range = [str]

    class superName(Property):
        domain = [Character]
        range = [str]

    class videoGames(Property):
        domain = [Character]
        range = [str]

    class hasWeaponsEquipment(Property):
        domain = [Character]
        range = [str]

    class hasTrope(Property):
        domain = [Character]
        range = [Trope]

    class hasDied(Property):
        domain = [Character]
        range = [bool]

    class isWoman(Property):
        domain = [Character]
        range = [bool]

    class isMan(Property):
        domain = [Character]
        range = [bool]

    class isNonBinary(Property):
        domain = [Character]
        range = [bool]

# Save the ontology
onto.save(file="your_ontology.owl", format="rdfxml")
