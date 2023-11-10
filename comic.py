import requests

apikey = "a26b0a0256b9ce48bb14c97059c9d85646a41991"
url = "http://comicvine.gamespot.com/api"

from simyan.comicvine import Comicvine
from simyan.sqlite_cache import SQLiteCache
from bs4 import BeautifulSoup

session = Comicvine(api_key=apikey, cache=SQLiteCache())

def get_comic_character_info(folder_info, character_name, url):
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "lxml")
    image = soup.find_all("img")[0]
    file_name = folder_info + "/" + folder_info + "_" + "Photo" + '.txt'
    with open(file_name, 'w') as file:
        file.write(image['src'])

    div_characters = soup.find_all("div", {"class":"wiki-details"})[0]


    # Initialize a dictionary to store the extracted data
    data = {}


    rows = div_characters.find_all('tr')
    for row in rows:
        # Extract the header and data from each row
        header = row.find('th').text.strip()
        if header == 'Powers' or header == 'Died':
            data_cell = row.find("div", {"class":"wiki-item-display"}).text.strip()
        else:
            data_cell = row.find('span').text.strip()
        # Store the data in the dictionary
        data[header] = data_cell

    # put each header and value in a new file
    for header, value in data.items():
        file_name = folder_info + "/" + folder_info + "_" + header + '.txt'
        with open(file_name, 'w') as file:
            file.write(value)
        print(f'Saved text from {header} to {file_name}')
        print()


        results = session.list_characters(params={"filter": "name:" + character_name})
        character = results[0]

        summary = character.summary
        # Save summary into a file
        with open(folder_info + "/" + folder_info + "_summary.txt", "w") as f:
            f.write(summary)


        description = character.description

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
            file_name = folder_info + "/" + folder_info + "_" + h2.get_text().strip().replace(' ', '_') + '.txt'


            with open(file_name, 'w') as file:
                file.write(content)

            print(f'Saved text from <h2> tag {index + 1} to {file_name}')


get_comic_character_info("emma_frost", "Emma Frost", "https://comicvine.gamespot.com/emma-frost/4005-1457/")
get_comic_character_info("cassandra_cain", "Cassandra Cain", "https://comicvine.gamespot.com/cassandra-cain/4005-65230/")
get_comic_character_info("midnighter", "Midnighter", "https://comicvine.gamespot.com/midnighter/4005-2196/")
get_comic_character_info("deadpool", "Deadpool", "https://comicvine.gamespot.com/deadpool/4005-7606/")
get_comic_character_info("wally_west", "Wally West", "https://comicvine.gamespot.com/wally-west/4005-23879/")