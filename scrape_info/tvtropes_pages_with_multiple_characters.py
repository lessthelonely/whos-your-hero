import requests
from bs4 import BeautifulSoup

def get_character_info(character_name, folder_info, url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")

    folders = soup.find_all("div",{"class": "folderlabel"})
    for index, h in enumerate(folders):
        if character_name in h.text:
            first_folder_label = h
            second_folder_label = folders[index+1]

            elements_between = []
            current_element = first_folder_label.find_next()

            while current_element != second_folder_label:
                elements_between.append(current_element)
                current_element = current_element.find_next()

            break
    
    li_elements = []  # To store the <li> elements

    for element in elements_between:
        if element.name == 'li':
            li_elements.append(element)


    print(li_elements)
        
    with open(folder_info + "/" + folder_info + "_Tropes.txt", "w", encoding="utf-8") as f:
        for t in li_elements:
            f.write(t.text + "\n")

get_character_info("Cassandra Cain", "cassandra_cain", "https://tvtropes.org/pmwiki/pmwiki.php/Characters/Batgirl")