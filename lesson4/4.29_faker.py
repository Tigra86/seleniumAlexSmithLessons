import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker


driver = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()
time.sleep(1)

valid_login = "standard_user"
valid_password = "secret_sauce"

fake = Faker()
first_name = fake.first_name()
last_name = fake.last_name()
zip_code = fake.zipcode()

user_name_field = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name_field.send_keys(valid_login)
print("Enter login")

user_password_field = driver.find_element(By.XPATH, "//input[@id='password']")
user_password_field.send_keys(valid_password)
print("Enter password")

login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
login_button.click()
print("Click Login button")

"""INFO Product #1"""
product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
product_1_name = product_1.text
print(product_1_name)

price_product_1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
price_product_1_amount = price_product_1.text
print(price_product_1_amount)

select_product_1 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
select_product_1.click()
print("Select Product 1")

cart_icon = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
cart_icon.click()
print("Enter Cart")

checkout_button = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkout_button.click()
print("Click Checkout button")

"""Select User INFO"""
first_name_field = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name_field.send_keys(first_name)
print("Enter first name")

last_name_field = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name_field.send_keys(last_name)
print("Enter last name")

zipcode_field = driver.find_element(By.XPATH, "//input[@id='postal-code']")
zipcode_field.send_keys(zip_code)
print("Enter zipcode")

time.sleep(3)
