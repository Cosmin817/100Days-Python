import requests
from bs4 import BeautifulSoup

# URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
response.raise_for_status()

plain_html_page = response.text

soup = BeautifulSoup(plain_html_page, "html.parser")
all_titles = [title.getText() for title in soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")]
all_titles.reverse()

with open("./movies.txt", 'w') as file:
    for movie in all_titles:
        file.write(f"{movie}\n")

