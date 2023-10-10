import requests
from bs4 import BeautifulSoup

URL = "https://tvtropes.org/pmwiki/pmwiki.php/Characters/Batgirl"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "lxml")
div_characters = soup.find("div", id="main-article")
# print(div_characters)
# search for "Cassandra Cain" in the div


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

if "Cassandra Cain" in soup.find_all("div",{"class": "folderlabel"})[3].text:
    after_h2 = soup.find_all("div",{"class": "folderlabel"})[3].find_all_next()

li_elements = []  # To store the <li> elements

for element in after_h2:
    if element.name == 'li':
        li_elements.append(element)

print(li_elements)
a_list = []
for li in li_elements:
    a_element = li.find('a')
    if a_element and a_element.get('href', '').startswith('/pmwiki/pmwiki.php') and not a_element.get('class') == ['twikilink']:
        break
    else:
        a_list.append(li.text)
print(a_list)
"""
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
"""