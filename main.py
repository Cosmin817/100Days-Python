from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# ganat59865@gyxmz.com/ganat59865 (LinkedIn Account)

URL="https://www.linkedin.com/jobs/search/?currentJobId=3780194441&f_AL=true&geoId=102257491&keywords=Python%20Developer&location=London%2C%20England%2C%20United%20Kingdom&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")

drive = webdriver.Chrome(options=chrome_options)
drive.get(URL)

sleep(0.5)
accept_cookies = drive.find_element(By.XPATH, value='/html/body/div[1]/div/section/div/div[2]/button[1]')
accept_cookies.click()

sleep(0.5)
sign_in = drive.find_element(By.LINK_TEXT, value="Sign in")
sign_in.click()

sleep(0.5)
enter_username = drive.find_element(By.ID, value="username")
enter_username.send_keys("ganat59865@gyxmz.com")

sleep(0.5)
enter_username = drive.find_element(By.ID, value="password")
enter_username.send_keys("ganat59865")

sleep(0.5)
log_in = drive.find_element(By.CSS_SELECTOR, value="button[aria-label='Sign in']")
log_in.click()
