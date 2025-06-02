from selenium import webdriver
from bs4 import BeautifulSoup

url = f'https://www.auto24.ee/kasutatud/nimekiri.php?bn=2&a=100&aj=&ae=8&af=100&otsi=otsi'


driver = webdriver.Firefox()

driver.get(url)

response = driver.page_source

soup = BeautifulSoup(response)

for card in soup.find_all('div', class_ = "result-row"):
    image = card.find('span', class_ = "thumb")
    # Show image url which was in HTML element
    print(image.get("style")[23:-2])

    # Find the description
    desc = card.find('div', class_ = "description")
    
    # Find the title, model, short model and price
    title = desc.find("span")
    model = desc.find("span", class_ = "model")
    short_model = desc.find("span", class_ = "model-short")
    price = desc.find("span", class_ = "price")

    if short_model is not None:
        # Show text which was in HTML elements
        print(title.get_text())
        print(model.get_text())
        print(short_model.get_text())
        # Encoding strings and convert from str to int
        print(int(price.get_text(strip=True)[:-2].replace(" ", "").replace('\xa0', '')))