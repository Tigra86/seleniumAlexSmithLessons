import time

from selenium import webdriver


class Start_class:
    def select_product(self):
        driver = webdriver.Chrome()
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()

        time.sleep(3)


test = Start_class()
test.select_product()
