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

print("Welcome to our Internet shop")
user_choice = int(input("Please select one of our products by  typing any number from 1 to 6: "))

if user_choice == 1:
    print("You've selected Sauce Labs Backpack")
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
                              (By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div"))
    finish_price_product_1_amount = finish_price_product_1.text
    print(finish_price_product_1_amount)
    assert price_product_1_amount == finish_price_product_1_amount, (f"Wrong price for product #1 is displaying on "
                                                                     f"the Summary page: {finish_price_product_1_amount}")
    print("Correct price for product #1 is displaying on the Summary page")

    summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]")
    summary_price_amount = summary_price.text
    print(summary_price_amount)

    total_price = f"Item total: {price_product_1_amount}"
    print(total_price)
    assert summary_price_amount == total_price, f"Total price is incorrect: {price_product_1_amount}"
    print("Total price is correct")

    time.sleep(3)

elif user_choice == 2:
    print("You've selected Sauce Labs Bike Light")
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

    """INFO Cart Product #2"""
    cart_product_2 = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
    cart_product_2_name = cart_product_2.text
    print(cart_product_2_name)
    assert product_2_name == cart_product_2_name, (f"Wrong product name for product #2 is displaying on the Cart page: "
                                                   f"{cart_product_2_name}")
    print("Correct product name for product #2 is displaying on the Cart page")

    cart_price_product_2 = (driver.find_element
                            (By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div"))
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
    first_name_field.send_keys(first_name)
    print("Enter first name")

    last_name_field = driver.find_element(By.XPATH, "//input[@id='last-name']")
    last_name_field.send_keys(last_name)
    print("Enter last name")

    zipcode_field = driver.find_element(By.XPATH, "//input[@id='postal-code']")
    zipcode_field.send_keys(zip_code)
    print("Enter zipcode")

    continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
    continue_button.click()
    print("Click Continue button")

    """INFO Finish Product #2"""
    finish_product_2 = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
    finish_product_2_name = finish_product_2.text
    print(finish_product_2_name)
    assert product_2_name == finish_product_2_name, (f"Wrong product name for product #2 is displaying on the Summary "
                                                     f"page: {finish_product_2_name}")
    print("Correct product name for product #2 is displaying on the Summary page")

    finish_price_product_2 = (driver.find_element
                              (By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div"))
    finish_price_product_2_amount = finish_price_product_2.text
    print(finish_price_product_2_amount)
    assert price_product_2_amount == finish_price_product_2_amount, (f"Wrong price for product #2 is displaying on "
                                                                     f"the Summary page: {finish_price_product_2_amount}")
    print("Correct price for product #2 is displaying on the Summary page")

elif user_choice == 3:
    print("You've selected Sauce Labs Bolt T-Shirt")
    """INFO Product #3"""
    product_3 = driver.find_element(By.XPATH, "//a[@id='item_1_title_link']")
    product_3_name = product_3.text
    print(product_3_name)

    price_product_3 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div")
    price_product_3_amount = price_product_3.text
    print(price_product_3_amount)

    select_product_3 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
    select_product_3.click()
    print("Select Product 3")

    cart_icon = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
    cart_icon.click()
    print("Enter Cart")

    """INFO Cart Product #3"""
    cart_product_3 = driver.find_element(By.XPATH, "//a[@id='item_1_title_link']")
    cart_product_3_name = cart_product_3.text
    print(cart_product_3_name)
    assert product_3_name == cart_product_3_name, (f"Wrong product name for product #3 is displaying on the Cart page: "
                                                   f"{cart_product_3_name}")
    print("Correct product name for product #3 is displaying on the Cart page")

    cart_price_product_3 = (driver.find_element
                            (By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div"))
    cart_price_product_3_amount = cart_price_product_3.text
    print(cart_price_product_3_amount)
    assert price_product_3_amount == cart_price_product_3_amount, (f"Wrong price for product #3 is displaying on "
                                                                   f"the Cart page: {cart_price_product_3_amount}")
    print("Correct price for product #2 is displaying on the Cart page")

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

    continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
    continue_button.click()
    print("Click Continue button")

    """INFO Finish Product #3"""
    finish_product_3 = driver.find_element(By.XPATH, "//a[@id='item_1_title_link']")
    finish_product_3_name = finish_product_3.text
    print(finish_product_3_name)
    assert product_3_name == finish_product_3_name, (f"Wrong product name for product #2 is displaying on the Summary "
                                                     f"page: {finish_product_3_name}")
    print("Correct product name for product #3 is displaying on the Summary page")

    finish_price_product_3 = (driver.find_element
                              (By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div"))
    finish_price_product_3_amount = finish_price_product_3.text
    print(finish_price_product_3_amount)
    assert price_product_3_amount == finish_price_product_3_amount, (f"Wrong price for product #3 is displaying on "
                                                                     f"the Summary page: {finish_price_product_3_amount}")
    print("Correct price for product #3 is displaying on the Summary page")

elif user_choice == 4:
    print("You've selected Sauce Labs Fleece Jacket")
    """INFO Product #4"""
    product_4 = driver.find_element(By.XPATH, "//a[@id='item_5_title_link']")
    product_4_name = product_4.text
    print(product_4_name)

    price_product_4 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[4]/div[2]/div[2]/div")
    price_product_4_amount = price_product_4.text
    print(price_product_4_amount)

    select_product_4 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
    select_product_4.click()
    print("Select Product 4")

    cart_icon = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
    cart_icon.click()
    print("Enter Cart")

    """INFO Cart Product #4"""
    cart_product_4 = driver.find_element(By.XPATH, "//a[@id='item_5_title_link']")
    cart_product_4_name = cart_product_4.text
    print(cart_product_4_name)
    assert product_4_name == cart_product_4_name, (f"Wrong product name for product #4 is displaying on the Cart page: "
                                                   f"{cart_product_4_name}")
    print("Correct product name for product #4 is displaying on the Cart page")

    cart_price_product_4 = (driver.find_element
                            (By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div"))
    cart_price_product_4_amount = cart_price_product_4.text
    print(cart_price_product_4_amount)
    assert price_product_4_amount == cart_price_product_4_amount, (f"Wrong price for product #4 is displaying on "
                                                                   f"the Cart page: {cart_price_product_4_amount}")
    print("Correct price for product #4 is displaying on the Cart page")

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

    continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
    continue_button.click()
    print("Click Continue button")

    """INFO Finish Product #4"""
    finish_product_4 = driver.find_element(By.XPATH, "//a[@id='item_5_title_link']")
    finish_product_4_name = finish_product_4.text
    print(finish_product_4_name)
    assert product_4_name == finish_product_4_name, (f"Wrong product name for product #4 is displaying on the Summary "
                                                     f"page: {finish_product_4_name}")
    print("Correct product name for product #4 is displaying on the Summary page")

    finish_price_product_4 = (driver.find_element
                              (By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div"))
    finish_price_product_4_amount = finish_price_product_4.text
    print(finish_price_product_4_amount)
    assert price_product_4_amount == finish_price_product_4_amount, (f"Wrong price for product #4 is displaying on "
                                                                     f"the Summary page: {finish_price_product_4_amount}")
    print("Correct price for product #4 is displaying on the Summary page")

elif user_choice == 5:
    print("You've selected Sauce Labs Onesie")
    """INFO Product #5"""
    product_5 = driver.find_element(By.XPATH, "//a[@id='item_2_title_link']")
    product_5_name = product_5.text
    print(product_5_name)

    price_product_5 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[5]/div[2]/div[2]/div")
    price_product_5_amount = price_product_5.text
    print(price_product_5_amount)

    select_product_5 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']")
    select_product_5.click()
    print("Select Product 5")

    cart_icon = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
    cart_icon.click()
    print("Enter Cart")

    """INFO Cart Product #5"""
    cart_product_5 = driver.find_element(By.XPATH, "//a[@id='item_2_title_link']")
    cart_product_5_name = cart_product_5.text
    print(cart_product_5_name)
    assert product_5_name == cart_product_5_name, (f"Wrong product name for product #5 is displaying on the Cart page: "
                                                   f"{cart_product_5_name}")
    print("Correct product name for product #5 is displaying on the Cart page")

    cart_price_product_5 = (driver.find_element
                            (By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div"))
    cart_price_product_5_amount = cart_price_product_5.text
    print(cart_price_product_5_amount)
    assert price_product_5_amount == cart_price_product_5_amount, (f"Wrong price for product #5 is displaying on "
                                                                   f"the Cart page: {cart_price_product_5_amount}")
    print("Correct price for product #5 is displaying on the Cart page")

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

    continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
    continue_button.click()
    print("Click Continue button")

    """INFO Finish Product #5"""
    finish_product_5 = driver.find_element(By.XPATH, "//a[@id='item_2_title_link']")
    finish_product_5_name = finish_product_5.text
    print(finish_product_5_name)
    assert product_5_name == finish_product_5_name, (f"Wrong product name for product #5 is displaying on the Summary "
                                                     f"page: {finish_product_5_name}")
    print("Correct product name for product #5 is displaying on the Summary page")

    finish_price_product_5 = (driver.find_element
                              (By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div"))
    finish_price_product_5_amount = finish_price_product_5.text
    print(finish_price_product_5_amount)
    assert price_product_5_amount == finish_price_product_5_amount, (f"Wrong price for product #5 is displaying on "
                                                                     f"the Summary page: {finish_price_product_5_amount}")
    print("Correct price for product #5 is displaying on the Summary page")

elif user_choice == 6:
    print("You've selected Test.allTheThings() T-Shirt (Red)")
    """INFO Product #6"""
    product_6 = driver.find_element(By.XPATH, "//a[@id='item_3_title_link']")
    product_6_name = product_6.text
    print(product_6_name)

    price_product_6 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[6]/div[2]/div[2]/div")
    price_product_6_amount = price_product_6.text
    print(price_product_6_amount)

    select_product_6 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
    select_product_6.click()
    print("Select Product 6")

    cart_icon = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
    cart_icon.click()
    print("Enter Cart")

    """INFO Cart Product #6"""
    cart_product_6 = driver.find_element(By.XPATH, "//a[@id='item_3_title_link']")
    cart_product_6_name = cart_product_6.text
    print(cart_product_6_name)
    assert product_6_name == cart_product_6_name, (f"Wrong product name for product #6 is displaying on the Cart page: "
                                                   f"{cart_product_6_name}")
    print("Correct product name for product #6 is displaying on the Cart page")

    cart_price_product_6 = (driver.find_element
                            (By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div"))
    cart_price_product_6_amount = cart_price_product_6.text
    print(cart_price_product_6_amount)
    assert price_product_6_amount == cart_price_product_6_amount, (f"Wrong price for product #6 is displaying on "
                                                                   f"the Cart page: {cart_price_product_6_amount}")
    print("Correct price for product #6 is displaying on the Cart page")

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

    continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
    continue_button.click()
    print("Click Continue button")

    """INFO Finish Product #6"""
    finish_product_6 = driver.find_element(By.XPATH, "//a[@id='item_3_title_link']")
    finish_product_6_name = finish_product_6.text
    print(finish_product_6_name)
    assert product_6_name == finish_product_6_name, (f"Wrong product name for product #6 is displaying on the Summary "
                                                     f"page: {finish_product_6_name}")
    print("Correct product name for product #6 is displaying on the Summary page")

    finish_price_product_6 = (driver.find_element
                              (By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div"))
    finish_price_product_6_amount = finish_price_product_6.text
    print(finish_price_product_6_amount)
    assert price_product_6_amount == finish_price_product_6_amount, (f"Wrong price for product #6 is displaying on "
                                                                     f"the Summary page: {finish_price_product_6_amount}")
    print("Correct price for product #6 is displaying on the Summary page")

else:
    print("Please enter number between 1 and 6")
