import requests
from bs4 import BeautifulSoup
import re
from filler_bot import GoogleFormFiller

# Google Forms: https://docs.google.com/forms/d/e/1FAIpQLSdLVUScmkqGuHRufTKabZH_uYz2q2pFcORcdsoAfV9gDuzkeQ/viewform?usp=sf_link
# Renting site: https://appbrewery.github.io/Zillow-Clone/

URL_RENTING_SITE = "https://appbrewery.github.io/Zillow-Clone/"
URL_GFORM = "https://docs.google.com/forms/d/e/1FAIpQLSdLVUScmkqGuHRufTKabZH_uYz2q2pFcORcdsoAfV9gDuzkeQ/viewform?usp=sf_link"
response_renting_site = requests.get(url=URL_RENTING_SITE)
response_renting_site.raise_for_status()

renting_site_plain_html = response_renting_site.text


soup = BeautifulSoup(renting_site_plain_html, "html.parser")
scraped_articles = soup.find_all('article')

article_links_list = []
addresses_list = []
prices_list = []

my_gfiller = GoogleFormFiller(url=URL_GFORM)

for scraped_article in scraped_articles:
    articles = scraped_article.find_all('a', attrs={"data-test": "property-card-link", "class": "property-card-link"})
    for a in articles:
        article_links_list.append(a["href"])

    addresses = scraped_article.find_all('address', attrs={"data-test": "property-card-addr"})
    for address in addresses:
        addresses_list.append(address.get_text(strip=True).replace('|', ','))

    prices = scraped_article.find_all('span', attrs={"data-test": "property-card-price"})
    for price in prices:
        price_text = price.text
        regex_price = re.search(r'\$[0-9]*[,]*[0-9]*', price_text).group()
        prices_list.append(regex_price)

my_gfiller.set_data(article_links_list, addresses_list, prices_list)
my_gfiller.fill_gform()