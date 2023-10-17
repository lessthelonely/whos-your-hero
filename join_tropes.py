# join all tropes in a set to call trope_description.py
all_tropes = set()

def get_tropes(folder_name):
    with open(folder_name + "/" + folder_name +"_TropeNames.txt", "r", encoding="utf-8") as f:
        tropes = f.readlines()
        tropes = [t.strip() for t in tropes]
        for t in tropes:
            all_tropes.add(t)

get_tropes("cassandra_cain")
get_tropes("emma_frost")
get_tropes("wally_west")
get_tropes("deadpool")
get_tropes("midnighter")

bonus_tropes = set()
with open("all_tropes_clean.txt", "w", encoding="utf-8") as f:
    with open("all_tropes.txt", "w", encoding="utf-8") as f1:
        for t in all_tropes:
            #check if there's / and join them if there is no spaces between the / and letters
            #if there's spaces between the / and letters, make 2 words
            t1 = t
            if "/" in t:
                #check if there's a space after the /
                if t[t.index("/") + 1] == " ":
                    # split the string into 2 words
                    words = t.split("/")
                    t = words[0]
                    t1 = words[0]
                    bonus_tropes.add(words[1])
                else:
                    t = t.replace("/", "")
            
            f1.write(t1 + "\n")

            #check if there's spaces and join them
            if " " in t:
                t = t.replace(" ", "")
    
            #check if there's apostrophes and join them
            if "'" in t:
                t = t.replace("'", "")
    
            #check if there's dashes and join them
            if "-" in t:
                t = t.replace("-", "")
    
            #check if there's commas and join them
            if "," in t:
                t = t.replace(",", "")
    
            #check if there's periods or exclamation points and delete them
            if "." in t:
                t = t.replace(".", "")
            if "!" in t:
                t = t.replace("!", "")
            if "?" in t:
                t = t.replace("?", "")

            f.write(t + "\n")

        for b in bonus_tropes:
            f1.write(b + "\n")

            #check if there's spaces and join them
            if " " in b:
                b = b.replace(" ", "")
    
            #check if there's apostrophes and join them
            if "'" in b:
                b = b.replace("'", "")
    
            #check if there's dashes and join them
            if "-" in b:
                b = b.replace("-", "")
    
            #check if there's commas and join them
            if "," in b:
                b = b.replace(",", "")
    
            #check if there's periods or exclamation points and delete them
            if "." in b:
                b = b.replace(".", "")
            if "!" in b:
                b = b.replace("!", "")
            if "?" in b:
                b = b.replace("?", "")

            f.write(b + "\n")
