import time

from selenium import webdriver


class StartClass:
    def select_product(self):
        driver = webdriver.Chrome()
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()

        time.sleep(3)


test = StartClass()
test.select_product()
