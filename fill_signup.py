from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")

URL = "https://secure-retreat-92358.herokuapp.com/"
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Azorel")

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Cutu")

email = driver.find_element(By.NAME, value="email")
email.send_keys("cutucutu@gmail.com")
email.send_keys(Keys.ENTER)