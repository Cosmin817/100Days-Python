import requests
from bs4 import BeautifulSoup
from pprint import pprint

URL = "https://www.amazon.com/Samsung-LC27F398FWNXZA-C27F398-Curved-Monitor/dp/B01CX26WIG/ref=sr_1_1?qid=1701546794&refinements=p_89%3ASAMSUNG&rnid=2528832011&s=computers-intl-ship&sr=1-1&th=1"

response_get_product_html_page = requests.get(url=URL)
response_get_product_html_page.raise_for_status()

soup = BeautifulSoup(response_get_product_html_page.text, "html.parser")
# pprint(soup.select("span[class="a-offscreen"]')

div_element = soup.find_all("div[data-csa-c-type][data-csa-c-slot-id][data-csa-c-content-id][data-csa-c-id]")

print(div_element)

# children = div.findChildren("span", recursive=True)
#
# for child in children:
#     print(child)
