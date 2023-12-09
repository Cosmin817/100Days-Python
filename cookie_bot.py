from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep, time


def check_available_products() -> list:
    available_products = []
    for i in range(0, 20):
        get_cursor_price = drive.find_element(By.ID, f"productPrice{i}").text
        if get_cursor_price != '':
            available_products.append([f"productPrice{i}", get_cursor_price])
    return available_products


def check_and_buy_product(fcookies_info_list: list, favailable_products: list):
    current_nr_of_cookies = int(fcookies_info_list[0].replace(",", ""))
    favailable_products = favailable_products
    for product in favailable_products[::-1]:

        if " million" in product[1]:
            product_price0 = product[1].replace(" million", "")
            product_price = int(product_price0.replace(".", "")) * (10**6)
        elif " billion" in product[1]:
            product_price0 = product[1].replace(" billion", "")
            product_price = int(product_price0.replace(".", "")) * (10**9)
        elif " trillion" in product[1]:
            product_price0 = product[1].replace(" trillion", "")
            product_price = int(product_price0.replace(".", "")) * (10**12)
        elif " quadrillion" in product[1]:
            product_price0 = product[1].replace(" quadrillion", "")
            product_price = int(product_price0.replace(".", "")) * (10**18)
        elif " quintillion" in product[1]:
            product_price0 = product[1].replace(" quintillion", "")
            product_price = int(product_price0.replace(".", "")) * (10**21)
        elif " sextillion" in product[1]:
            product_price0 = product[1].replace(" sextillion", "")
            product_price = int(product_price0.replace(".", "")) * (10**21)
        elif " septillion" in product[1]:
            product_price0 = product[1].replace(" septillion", "")
            product_price = int(product_price0.replace(".", "")) * (10**24)
        else:
            product_price = int(product[1].replace(",", ""))

        if product_price <= current_nr_of_cookies:
            print(f"Buy product {product}")
            favailable_product_index = str(favailable_products.index(product))
            print(favailable_product_index)
            buy_product = drive.find_element(By.ID, value=f"product{favailable_product_index}")
            buy_product.click()
            break

URL = "https://orteil.dashnet.org/cookieclicker/"
timeout = time() + 60*10   # 5 minutes from now

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
while time() <= timeout:
    big_cookie.click()
    if time() >= timer_5sec:
        cookies_info_list = str(drive.find_element(By.ID, value="cookies").text).split()
        # 1st element is the current number of cookies.
        # 2nd element is the cookies per second.
        for word in 'cookies', 'per', 'second:':
            cookies_info_list.remove(word)
        print(cookies_info_list)
        available_products = check_available_products()
        check_and_buy_product(cookies_info_list, available_products)
        timer_5sec = time() + 5

#product0 = Cursor
#product1 = Grandma
#product2 = Farm
#product3 = Mine
#product4 = Factory
#product5 = Bank