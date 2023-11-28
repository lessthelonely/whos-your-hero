import requests
from bs4 import BeautifulSoup

def get_trope_description(url):
    url_start = "https://tvtropes.org"
    url_trope = "https://tvtropes.org/pmwiki/pmwiki.php/Main/"

    full_url = url_trope + url
    page = requests.get(full_url)
    soup = BeautifulSoup(page.content, "lxml")
    find_text = soup.find("div", {"id": "main-article"}).find_all("p")

    # reorder the list

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


get_trope_description("ActionHero")