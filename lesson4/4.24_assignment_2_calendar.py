import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.maximize_window()

today = datetime.now()  # Got today's date
time_delta = timedelta(days=10)  # Created a variable with the 10 days difference
new_date = today + time_delta  # Created a variable with the date 10 days from now
future_date = new_date.strftime("%m/%d/%Y")  # Changed the date format to match calendar date

calendar_field = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
calendar_field.send_keys(Keys.COMMAND + "a")
calendar_field.send_keys(Keys.BACKSPACE)
calendar_field.send_keys(future_date)
calendar_field.send_keys(Keys.RETURN)

time.sleep(3)
