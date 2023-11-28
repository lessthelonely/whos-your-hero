def get_tropes_names(folder_name):
    trope_names = []
    with open(folder_name + "/" + folder_name +"_Tropes.txt", "r", encoding="utf-8") as f:
        tropes = f.readlines()
        tropes = [t.strip() for t in tropes]

        for t in tropes:
            trope_names.append(t.split(":")[0])
        print(trope_names)

    with open(folder_name + "/" + folder_name +"_TropeNames.txt", "w", encoding="utf-8") as f:
        for t in trope_names:
            f.write(t + "\n")

#get_tropes_names("cassandra_cain")
#get_tropes_names("emma_frost")
#get_tropes_names("wally_west")
#get_tropes_names("deadpool")
#get_tropes_names("midnighter")
get_tropes_names("cyclops")

