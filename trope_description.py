import requests
from bs4 import BeautifulSoup

def get_trope_description(url):
    url_start = "https://tvtropes.org"
    url_trope = "https://tvtropes.org/pmwiki/pmwiki.php/Main/"

    if url == "Catchphrase":
        full_url = url_trope + "CharacterCatchphrase" #catchphrase is under construction so we have this special case
    elif url == "NoGoodDeed":
        full_url = url_trope + "NoGoodDeedGoesUnpunished" #NoGoodDeed is under construction so we have this special case
    else:
        full_url = url_trope + url
    page = requests.get(full_url)
    soup = BeautifulSoup(page.content, "lxml")
    find_text = soup.find("h2").find_all_previous("p")
    # reorder the list
    find_text.reverse()
    find_text = find_text[4:]

    text = ""
    for t in find_text:
        # Extract the text within the paragraph (p) tag
        paragraph_text = t.text

        # Find the anchor (a) tag within the HTML
        link_tag = t.find('a')

        if link_tag is None:
            text += paragraph_text
            continue

        # Extract the text within the anchor tag
        link_text = link_tag.text

        # Extract the link (href) attribute
        link = url_start + link_tag['href']

        # Create the formatted text by replacing the link within square brackets
        formatted_text = paragraph_text.replace(link_text, f"{link_text} [\"{link}\"]")
        text += formatted_text

        with open("tropes/" + url + ".txt", "w", encoding="utf-8") as f:
            f.write(text)


# read the tropes from the file
tropes_url = []
with open("all_tropes_clean.txt", "r", encoding="utf-8") as f:
    tropes_url = f.readlines()
    tropes_url = [t.strip() for t in tropes_url]

for t in tropes_url:
    print(t)
    get_trope_description(t)

#PopCulturedBadass - page different 
# see what the hell is up with this -> StepfordSnarker; StatuesqueStunner, UselessAccessory, WillTheyorWontThey, ElementalMotifs

