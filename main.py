from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

URL = "https://www.speedtest.net/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

sleep(0.5)
accept_privacy_button = driver.find_element(By.ID, value="onetrust-accept-btn-handler")
accept_privacy_button.click()

sleep(0.5)
start_test_button = driver.find_element(By.CLASS_NAME, value="start-text")
start_test_button.click()

sleep(60)
close_button = driver.find_element(By.XPATH, value="/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button")
close_button.click()

sleep(0.5)
get_download_speed = driver.find_element(By.XPATH, value="/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span")
download_speed = get_download_speed.text

sleep(0.5)
get_upload_speed = driver.find_element(By.XPATH, value="/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")
upload_speed = get_upload_speed.text

print(f"Download speed: {download_speed} Mb/s\nUpload speed: {upload_speed} Mb/s")
#result-data-large number result-data-value download-speed