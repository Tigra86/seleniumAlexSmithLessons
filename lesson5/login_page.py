from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Login_page:

    def __init__(self, driver):
        self.driver = driver

    def authorization(self, login, password):
        user_name_field = ("id", "user-name")
        user_password_field = ("id", "password")
        login_button = ("id", "login-button")
        wait = WebDriverWait(self.driver, 30, poll_frequency=1)
        wait.until(EC.element_to_be_clickable(user_name_field)).send_keys(login)
        print("Enter login")
        wait.until(EC.element_to_be_clickable(user_password_field)).send_keys(password)
        print("Enter password")
        wait.until(EC.element_to_be_clickable(login_button)).click()
        print("Click login button")
