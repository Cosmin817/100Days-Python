from bs4 import BeautifulSoup
import requests

#
# with open("website.html", "r", encoding="utf8") as f:
#     contents = f.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
#
# # print(soup.title.string)
#
# all_anchor_tags = soup.find_all(name="p")
# # print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     pass
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# #print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# #print(section_heading.get("class"))
#
#
# company_url = soup.select_one(selector="ul li")
# print(company_url)


response = requests.get(url="https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)

#first_title = soup.find_all(name="span", class_="titleline")

articles = soup.select(selector="tr[class]>td[class]>span[class]>a[href]")
article_texts = []
article_links = []

for article_tag in articles:
    # first_title = soup.find(name="a", class_="storylink")
    text = article_tag.getText()
    link = article_tag.get("href")
    article_texts.append(text)
    article_links.append(link)

article_upvotes = [int(score.getText().split(sep=' ', maxsplit=1)[0]) for score in soup.find_all(name="span", class_="score")]


print(article_texts)
print(article_links)
print(article_upvotes)


max_upvotes = max(article_upvotes)
max_upvotes_index = article_upvotes.index(max_upvotes)

high_article = article_texts[max_upvotes_index]
high_link = article_links[max_upvotes_index]
high_upvotes = article_upvotes[max_upvotes_index]
print(" ")
print(high_article)
print(high_link)
print(high_upvotes)