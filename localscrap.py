# simple web-scrapper example

import requests
from bs4 import BeautifulSoup
import rich


URL = 'http://localhost/movies.html'

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

movies = soup.find_all("li")

for mov in movies :
    # print(prod, end="\n"*2)

    title = mov.find("h4").find("a").get_text()
    url = mov.find("h4").find("a").get('href')
    info = mov.find("p").get_text()
    # print (title.get_text(), price.get_text())
    print(title, end="")
    print(" ("+ url +") ", end="")
    rich.print(' -> [cyan]'+ info.strip() +'[/cyan]')

    movie_info(url)





