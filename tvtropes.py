# Cassandra's page is different from the others because she shares it with the other batgirls
# Midnighter's page is the easiest one because he doesn't have any folders so let's start with his
# Apparently Midnighter has general tropes and tropes in folders

import requests
from bs4 import BeautifulSoup

def get_character_tropes(folder_info, url):

    
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "lxml")
    div_characters = soup.find("div", id="main-article")
    h2 = div_characters.find("h2")
    after_h2 = h2.find_all_next("ul")

    if soup.find("div",{"class": "folderlabel"}) != None:
        if folder_info == "midnighter":
            after_h2 += soup.find("div",{"class": "folderlabel"}).find_all_next("ul")
        else:
            after_h2 = soup.find("div",{"class": "folderlabel"}).find_all_next("ul")


    a_list = []
    for a in after_h2:
        li_element = a.find('li')
        a_element = li_element.find('a')
        if a_element and a_element.text == 'Identity Wars':
            a_list+=a
        elif a_element and a_element.get('href', '').startswith('/pmwiki/pmwiki.php') and not a_element.get('class') == ['twikilink']:
            break
        else:
            a_list+=a
    print(a_list)
    with open(folder_info + "/" + folder_info + "_Tropes.txt", "w", encoding="utf-8") as f:
        for t in a_list:
            f.write(t.text + "\n")

# get_character_tropes("midnighter", "https://tvtropes.org/pmwiki/pmwiki.php/Characters/TheAuthorityMidnighter")
# get_character_tropes("emma_frost", "https://tvtropes.org/pmwiki/pmwiki.php/Characters/MarvelComicsEmmaFrost")
# get_character_tropes("wally_west","https://tvtropes.org/pmwiki/pmwiki.php/Characters/TheFlashWallyWest")
get_character_tropes("deadpool", "https://tvtropes.org/pmwiki/pmwiki.php/Characters/DeadpoolWadeWilson")# get_character_tropes("deadpool", "https://tvtropes.org/pmwiki/pmwiki.php/Characters/DeadpoolWadeWilson")
get_character_tropes("cyclops", "https://tvtropes.org/pmwiki/pmwiki.php/Characters/MarvelComicsCyclops")