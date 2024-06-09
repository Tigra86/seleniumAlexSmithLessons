from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

data_products = {"1": "Sauce Labs Backpack",
                 "2": "Sauce Labs Bike Light",
                 "3": "Sauce Labs Bolt T-Shirt",
                 "4": "Sauce Labs Fleece Jacket",
                 "5": "Sauce Labs Onesie",
                 "6": "T-Shirt (Red)", }

print("Приветствую тебя в нашем интернет-магазине!\nВыбери один из следующих товаров и укажи его номер:")
[print(f"{number} - {product}") for number, product in data_products.items()]

while True:
    try:
        product_number = input()
        print(f"Выбранный товар: {data_products[product_number]}")
        break
    except KeyError:
        print('Ошибка! Введите номер товара из каталога от 1 до 6\nПовторите ввод:')

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)  # Открытие страницы по ссылке
driver.maximize_window()

'''Авторизация на сайте'''
login = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login)
print('Input login')

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print('Input password')

button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print('Click login button')

'''Информация по выбранному товару'''
product_text = driver.find_element(By.XPATH, f"(//div[@class='inventory_item_name '])[{product_number}]")
product_text_value = product_text.text
print(product_text_value)

product_price = driver.find_element(By.XPATH, f"(//div[@class='inventory_item_price'])[{product_number}]")
product_price_value = product_price.text
print(product_price_value)

'''Добавляем товар в корзину'''
button_add_to_cart = driver.find_element(By.XPATH,
                                         f"(//button[@class='btn btn_primary btn_small btn_inventory '])[{product_number}]")
button_add_to_cart.click()
print('Click button add to cart')

'''''Входим в корзину'''
cart = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
cart.click()
print('Click cart button')

''''Информация по выбранному товару в корзине'''
product_cart = driver.find_element(By.XPATH, "//div[@class='inventory_item_name']")
product_cart_value = product_cart.text
print(product_cart_value)

product_cart_price = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
product_cart_price_value = product_cart_price.text
print(product_cart_price_value)

'''Проверяем соответствие названия и цены выбранного товара в корзине'''
assert product_text_value == product_cart_value
print('Info product in cart - Good')

assert product_price_value == product_cart_price_value
print('Info price product in cart - Good')

checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkout.click()

''''Заполняем данные заказчика'''
first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys('Petr')
print('Input first name')

last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys('Petrenko')
print('Input last_name')

postal_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
postal_code.send_keys('123456')
print('Input postal_code')

''''Нажимаем продолжить'''
button_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
button_continue.click()
print('Click continue button')

''''Информация по выбранному товару финальное'''
product_finish = driver.find_element(By.XPATH, "//div[@class='inventory_item_name']")
product_finish_value = product_finish.text
print(product_finish_value)

product_finish_price = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
product_finish_price_value = product_finish_price.text
print(product_finish_price_value)

''''Проверяем соответствие названия и цены выбранного товара в финале'''
assert product_text_value == product_finish_value
print('Finish info product - Good')

assert product_price_value == product_finish_price_value
print('Finish price - Good')

'''Проверяем соответствует ли итоговая сумма'''
summary_price = driver.find_element(By.XPATH, "//div[@class='summary_subtotal_label']")
summary_price_value = summary_price.text
print(summary_price_value)

assert product_price_value == summary_price_value.split()[-1]
print('Finish summary price - Good')

'''Оформляем заказ'''
button_finish = driver.find_element(By.XPATH, "//button[@id='finish']")
button_finish.click()
print("Click finish button")
