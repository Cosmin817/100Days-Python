from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep, time

URL = "https://orteil.dashnet.org/cookieclicker/"
timeout = time() + 60*1   # 5 minutes from now

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")

drive = webdriver.Chrome(options=chrome_options)
drive.get(URL)

consent_button = drive.find_element(By.CLASS_NAME, value="fc-button-label")
consent_button.click()

sleep(2)

lang_button = drive.find_element(By.ID, value="langSelect-EN")
lang_button.click()

sleep(3)

big_cookie = drive.find_element(By.ID, value="bigCookie")

cookies_info = "NULL"

timer_5sec = time() + 5
# while time() <= timeout:
#     big_cookie.click()
#     if time() >= timer_5sec:
#         cookies_info_list = str(drive.find_element(By.ID, value="cookies").text).split()
#         # 1st element is the current number of cookies.
#         # 2nd element is the cookies per second.
#         for word in 'cookies', 'per', 'second:':
#             cookies_info_list.remove(word)
#         timer_5sec = time() + 5
#         print(cookies_info_list)

#product0 = Cursor
#product1 = Grandma
#product2 = Farm
#product3 = Mine
#product4 = Factory
#product5 = Bank

get_cursor_price = drive.find_element(By.ID, "productPrice0").text
print(get_cursor_price)


