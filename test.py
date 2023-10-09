import requests
from bs4 import BeautifulSoup

URL = "https://tvtropes.org/pmwiki/pmwiki.php/Series/Damages"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "lxml")
div_characters = soup.find("div", id="main-article")
# print(div_characters)
ps = div_characters.find("ul")
# print(ps)
characters = []
for p in ps:
    characters.append(p.text)
print("CHARACTERS:\n")
print(characters)
h2 = div_characters.find("h2")
# print(h2)
after_h2 = h2.find_all_next("ul")
#print(after_h2)


a_list = []
for a in after_h2:
    li_element = a.find('li')
    a_element = li_element.find('a')
    if a_element and a_element.get('href', '').startswith('/pmwiki/pmwiki.php') and not a_element.get('class') == ['twikilink']:
        break
    else:
        a_list+=a
print(a_list)
tropes = []
for t in a_list:
   tropes.append(t.text)
print("TROPES:\n")
print(tropes)

# print only after the spoiler
