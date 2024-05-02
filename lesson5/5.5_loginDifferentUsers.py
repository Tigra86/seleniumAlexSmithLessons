import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Login():
    def login_different_users(self):
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 10, poll_frequency=1)
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()
        time.sleep(1)

        print("Start test")
        usernames = [
            'standard_user',
            'locked_out_user',
            'problem_user',
            'performance_glitch_user',
            'error_user',
            'visual_user'
        ]
        valid_password = "secret_sauce"
        user_name_field = ("id", "user-name")
        user_password_field = ("id", "password")
        login_button = ("id", "login-button")
        error_msg_box = ("xpath", "//*[@id='login_button_container']//h3")
        products_page = ("xpath", "//*[@id='header_container']/div[2]/span")
        burger_button = ('id', 'react-burger-menu-btn')
        logout_button = ('css selector', '#logout_sidebar_link')

        for username in usernames:
            try:
                wait.until(EC.element_to_be_clickable(user_name_field)).send_keys(username)
                print("Enter login")

                wait.until(EC.element_to_be_clickable(user_password_field)).send_keys(valid_password)
                print("Enter password")

                wait.until(EC.element_to_be_clickable(login_button)).click()
                print("Click login button")

                assert wait.until(EC.visibility_of_element_located(products_page)), "You are on the wrong page"
                print("Verify correct page")

                wait.until(EC.element_to_be_clickable(burger_button)).click()
                print("Click burger button")

                wait.until(EC.element_to_be_clickable(logout_button)).click()
                print("Click logout button")

            except Exception:
                print("The error message is displaying (see below)")
                print(wait.until(EC.visibility_of_element_located(error_msg_box)).text)
                driver.refresh()


test = Login()
test.login_different_users()
