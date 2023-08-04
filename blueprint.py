import requests
from bs4 import BeautifulSoup
import rich

URL = 'https://www.sklavenitis.gr/galata-rofimata-chymoi-psygeioy/galata-psygeioy/'

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

products = soup.find_all("div", class_="product")

for prod in products :
    # print(prod, end="\n"*2)
    for span in prod.findAll("span") :
        span.replace_with('')
    title = prod.find("h4").find("a").get_text()
    price = prod.find("div", class_="price").get_text()
    # print (title.get_text(), price.get_text())
    rich.print(title.strip() +' -> [cyan]'+ price.strip() +'[/cyan]')
