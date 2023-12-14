from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class GoogleFormFiller:
    def __init__(self, url):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(url)
        self.article_links_list = list()
        self.addresses_list = list()
        self.prices_list = list()

    def set_data(self, article_links_list: list, addresses_list: list, prices_list: list) -> int:
        self.article_links_list = article_links_list
        self.addresses_list = addresses_list
        self.prices_list = prices_list
        return 0

    def get_article_links_list(self) -> list:
        return self.article_links_list

    def get_addresses_list(self) -> list:
        return self.addresses_list

    def get_prices_list(self) -> list:
        return self.prices_list

    def fill_gform(self):
        if not self.article_links_list or not self.addresses_list or not self.prices_list:
            raise Exception("Please set article_links_list, addresses_list, prices_list")
        sleep(0.5)

        for i in range(0, len(self.article_links_list)):
            input_property_adress = self.driver.find_element(By.XPATH,
                                                             value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]"
                                                                   "/div/div/div[2]/div/div[1]/div/div[1]/input")
            input_property_adress.send_keys(f"{self.addresses_list[i]}")

            input_price = self.driver.find_element(By.XPATH,
                                                   value="/html/body/div/div[2]/form/div[2]/div/div[2]"
                                                         "/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
            input_price.send_keys(f"{self.prices_list[i]}")

            input_link = self.driver.find_element(By.XPATH,
                                                  value="/html/body/div/div[2]/form/div[2]/div"
                                                        "/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
            input_link.send_keys(f"{self.article_links_list[i]}")

            send_form = self.driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]"
                                                                 "/div/div[3]/div[1]/div[1]/div")
            send_form.click()

            send_another = self.driver.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
            send_another.click()

        return 0






