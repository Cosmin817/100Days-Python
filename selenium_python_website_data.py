from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.python.org/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

events = str(driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul').text).split('\n')
events_sublist = [events[n:n+2] for n in range(0, len(events), 2)]

c = 0
output_dict = {}
for event in events_sublist:
    output_dict[c] = events_sublist[c]
    c += 1

print(output_dict)