import requests
from bs4 import BeautifulSoup

URL = 'https://www.sklavenitis.gr/galata-rofimata-chymoi-psygeioy/galata-psygeioy/'

def cyan(txt) :
    return "\033[1;36;48m" + txt +"\033[1;37;48m"

page = requests.get(URL)
if page.status_code == 404 : 
    print ('The Web Page was not found')
else :

    soup = BeautifulSoup(page.content, "html.parser")

    products = soup.find_all("div", class_="product")

    for prod in products :
        # print(prod, end="\n"*2)
        for span in prod.findAll("span") :
            span.replace_with('')
        title = prod.find("h4").find("a").get_text()
        price = prod.find("div", class_="price").get_text()
        # print (title.get_text(), price.get_text())
        print(title.strip(), '->' , cyan(price.strip()))
