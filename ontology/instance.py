from onto import Character 
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

load_aliases(["cassandra_cain"])

