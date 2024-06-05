import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()
time.sleep(1)

valid_login = "standard_user"
valid_password = "secret_sauce"

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

"""INFO Product #2"""
product_2 = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
product_2_name = product_2.text
print(product_2_name)

price_product_2 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div")
price_product_2_amount = price_product_2.text
print(price_product_2_amount)

select_product_2 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
select_product_2.click()
print("Select Product 2")

cart_icon = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
cart_icon.click()
print("Enter Cart")

"""INFO Cart Product #1"""
cart_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
cart_product_1_name = cart_product_1.text
print(cart_product_1_name)
assert product_1_name == cart_product_1_name, (f"Wrong product name for product #1 is displaying on the Cart page: "
                                               f"{cart_product_1_name}")
print("Correct product name for product #1 is displaying on the Cart page")

cart_price_product_1 = (driver.find_element
                        (By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div"))
cart_price_product_1_amount = cart_price_product_1.text
print(cart_price_product_1_amount)
assert price_product_1_amount == cart_price_product_1_amount, (f"Wrong price for product #1 is displaying on "
                                                               f"the Cart page: {cart_price_product_1_amount}")
print("Correct price for product #1 is displaying on the Cart page")

"""INFO Cart Product #2"""
cart_product_2 = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
cart_product_2_name = cart_product_2.text
print(cart_product_2_name)
assert product_2_name == cart_product_2_name, (f"Wrong product name for product #2 is displaying on the Cart page: "
                                               f"{cart_product_2_name}")
print("Correct product name for product #2 is displaying on the Cart page")

cart_price_product_2 = (driver.find_element
                        (By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/div"))
cart_price_product_2_amount = cart_price_product_2.text
print(cart_price_product_2_amount)
assert price_product_2_amount == cart_price_product_2_amount, (f"Wrong price for product #2 is displaying on "
                                                               f"the Cart page: {cart_price_product_2_amount}")
print("Correct price for product #2 is displaying on the Cart page")

checkout_button = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkout_button.click()
print("Click Checkout button")

"""Select User INFO"""
first_name_field = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name_field.send_keys("Tigran")
print("Enter first name")

last_name_field = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name_field.send_keys("Azaryan")
print("Enter last name")

zipcode_field = driver.find_element(By.XPATH, "//input[@id='postal-code']")
zipcode_field.send_keys("94132")
print("Enter zipcode")

continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
continue_button.click()
print("Click Continue button")

"""INFO Finish Product #1"""
finish_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
finish_product_1_name = finish_product_1.text
print(finish_product_1_name)
assert product_1_name == finish_product_1_name, (f"Wrong product name for product #1 is displaying on the Summary "
                                                 f"page: {finish_product_1_name}")
print("Correct product name for product #1 is displaying on the Summary page")

finish_price_product_1 = (driver.find_element
                          (By.XPATH,"//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div"))
finish_price_product_1_amount = finish_price_product_1.text
print(finish_price_product_1_amount)
assert price_product_1_amount == finish_price_product_1_amount, (f"Wrong price for product #1 is displaying on "
                                                                 f"the Summary page: {cart_price_product_1_amount}")
print("Correct price for product #1 is displaying on the Summary page")

"""INFO Finish Product #2"""
finish_product_2 = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
finish_product_2_name = finish_product_2.text
print(finish_product_2_name)
assert product_2_name == finish_product_2_name, (f"Wrong product name for product #2 is displaying on the Summary "
                                                 f"page: {finish_product_2_name}")
print("Correct product name for product #2 is displaying on the Summary page")

finish_price_product_2 = (driver.find_element
                          (By.XPATH,"//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div"))
finish_price_product_2_amount = finish_price_product_2.text
print(finish_price_product_2_amount)
assert price_product_2_amount == finish_price_product_2_amount, (f"Wrong price for product #2 is displaying on "
                                                                 f"the Summary page: {cart_price_product_2_amount}")
print("Correct price for product #2 is displaying on the Summary page")

summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]")
summary_price_amount = summary_price.text
print(summary_price_amount)

"""Use regular expression (re) to extract all decimal numbers from the string into a list and then convert the last item 
on the list into a number by using pop()"""
price_product_1 = re.findall("\d+\.\d+", finish_price_product_1_amount).pop()
price_product_2 = re.findall("\d+\.\d+", finish_price_product_2_amount).pop()

total_price = f"Item total: ${float(price_product_1) + float(price_product_2)}"
print(total_price)
assert summary_price_amount == total_price, (f"Total price is incorrect:"
                                             f" ${float(price_product_1) + float(price_product_2)}")
print("Total price is correct")

time.sleep(3)
