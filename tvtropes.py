# Cassandra's page is different from the others because she shares it with the other batgirls
# Midnighter's page is the easiest one because he doesn't have any folders so let's start with his

import requests
from bs4 import BeautifulSoup

URL = "https://tvtropes.org/pmwiki/pmwiki.php/Characters/TheAuthorityMidnighter"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "lxml")
div_characters = soup.find("div", id="main-article")
h2 = div_characters.find("h2")
after_h2 = h2.find_all_next("ul")


a_list = []
for a in after_h2:
    li_element = a.find('li')
    a_element = li_element.find('a')
    if a_element and a_element.get('href', '').startswith('/pmwiki/pmwiki.php') and not a_element.get('class') == ['twikilink']:
        break
    else:
        a_list+=a
# print(a_list)
tropes = []
with open("tropes.txt", "w", encoding="utf-8") as f:
    for t in a_list:
        tropes.append(t.text)
        f.write(t.text + "\n")


