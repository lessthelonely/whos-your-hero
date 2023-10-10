import requests

apikey = "a26b0a0256b9ce48bb14c97059c9d85646a41991"
url = "http://comicvine.gamespot.com/api"

from simyan.comicvine import Comicvine
from simyan.sqlite_cache import SQLiteCache
from bs4 import BeautifulSoup

URL = "https://comicvine.gamespot.com/emma-frost/4005-1457/"

page = requests.get(URL)


soup = BeautifulSoup(page.content, "lxml")
div_characters = soup.find_all("div", {"class":"wiki-details"})[0]


# Initialize a dictionary to store the extracted data
data = {}


rows = div_characters.find_all('tr')
for row in rows:
    # Extract the header and data from each row
    header = row.find('th').text.strip()
    if header == 'Powers':
        data_cell = row.find("div", {"class":"wiki-item-display"}).text.strip()
    else:
        data_cell = row.find('span').text.strip()
    # Store the data in the dictionary
    data[header] = data_cell

# put each header and value in a new file
for header, value in data.items():
    file_name = "emma_frost/emma_" + header + '.txt'
    with open(file_name, 'w') as file:
        file.write(value)
    print(f'Saved text from {header} to {file_name}')
    print()





"""
# Search for Publisher
results = session.list_characters(params={"filter": "name:Emma Frost"})
# Save data per character
emma = results[0]
alias = emma.aliases

# Save aliases into a file
# with open("emma_frost/emma_aliases.txt", "w") as f:
#     f.write(alias)

birth = emma.date_of_birth

description = emma.description

# Parse the HTML content
soup = BeautifulSoup(description, 'html.parser')

# Find all <h2> tags
h2_tags = soup.find_all('h2')
print(h2_tags)

# Create separate files for each <h2> tag
for index, h2 in enumerate(h2_tags):
    # Extract the text content of the <h2> tag using get_text()
    content = ''
    next_element = h2.find_next_sibling()
    while next_element and next_element.name != 'h2':
        if next_element.name == 'figure':
            content += ''
        else:
            if next_element.name == 'ul':
                li_elements = next_element.find('li')
                if li_elements != None:
                    for li_element in next_element.find_all('li'):
                        content += '\n' + str(li_element.get_text())
            if next_element.name == 'h3' or next_element.name == 'h4':
                content += '\n' + str(next_element.get_text()) + '\n'
            else:
                content += str(next_element.get_text())
        next_element = next_element.find_next_sibling()

    # Create a separate file for each <h2> tag
    file_name = "emma_frost/emma_" + h2.get_text().strip().replace(' ', '_') + '.txt'
    
    
    with open(file_name, 'w') as file:
        file.write(content)

    print(f'Saved text from <h2> tag {index + 1} to {file_name}')

# check tvtropes

def get_comic_info():









first_issue = emma.first_issue
summary = emma.summary
print("Alias: " + alias)
# print("Birth: " + birth)
#print("Description: " + description) # printing everything
print("First Issue: " + first_issue.name)

print("Summary: " + summary)


# results = session.list_characters(params={"filter": "name:Midnighter"})
# results = session.list_characters(params={"filter": "name:Cassandra Cain"})
# results = session.list_characters(params={"filter": "name:Deadpool"})
# results = session.list_characters(params={"filter": "name:Wally West"})

"""