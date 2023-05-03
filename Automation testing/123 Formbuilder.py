import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import random


driver = webdriver.Chrome()
driver.get("https://form.123formbuilder.com/5012215")
driver.maximize_window()  # driver.set_window_size(1200, 800)
driver.implicitly_wait(5)


print(driver.title)  # Website title
driver.find_element(By.XPATH, "//h1[contains(text(),'Order Form')]")  # filling in the form
time.sleep(2)
driver.find_element(By.XPATH, "//*[@placeholder='First']").send_keys("Malika")  # Customer first name
time.sleep(2)
driver.find_element(By.XPATH, "//*[@placeholder='Last']").send_keys("Azizova")  # Customer last name
time.sleep(2)
# random email
driver.find_element(By.XPATH, "//*[@type='email']").send_keys(str(random.randrange(1000, 9999)) + '@gmail.com')
time.sleep(2)
# random phone number
driver.find_element(By.XPATH, "//input[contains(@placeholder,'### ### #### ')]").send_keys(
    str(random.randrange(1, 9999999)).zfill(10))
time.sleep(2)
# Choose your preferred product
driver.find_element(By.XPATH, "//span[@data-role='option-text'][contains(.,'# Product 1')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[contains(@type,'number')]").send_keys(str(random.randint(1, 100))) # quantity
time.sleep(2)
# Delivery Date
element = driver.find_element(By.ID, "date-00000012-month")
action = ActionChains(driver)
action.click(on_element = element)
action.send_keys("04")
action.perform()

element = driver.find_element(By.ID, "date-00000012-day")
action = ActionChains(driver)
action.click(on_element = element)
action.send_keys("22")
action.perform()

element = driver.find_element(By.ID, "date-00000012-year")
action = ActionChains(driver)
action.click(on_element = element)
action.send_keys("2023")
action.perform()
# Delivery Address
driver.find_element(By.XPATH, "//*[@placeholder='Street Address']").send_keys("Main street")
driver.find_element(By.XPATH, "//*[@placeholder='Street Address Line 2']").send_keys("apt 4")

driver.find_element(By.XPATH, "//*[@placeholder='City']").send_keys(" Orlando")  # City
driver.find_element(By.XPATH, "//*[@placeholder='Region']").send_keys("Florida")  # Region
driver.find_element(By.XPATH, "//*[@placeholder='Postal / Zip Code']").send_keys("32801")  # Postal/Zip Code
driver.find_element(By.XPATH, "//*[@placeholder='Country']").send_keys("uni")  # Typing country name
driver.find_element(By.XPATH, "//div[@data-index='240'][contains(.,'United States')]").click()  # Clicking country name
# Dropdown menu
driver.find_element(By.XPATH, "//*[@value='Choice2']").click()
# Multiple choice section
driver.find_element(By.XPATH, "(//label[@data-role='checkbox'])[2]").click()
time.sleep(2)
driver.find_element(By.XPATH, "(//label[@data-role='checkbox'])[3]").click()
time.sleep(2)

driver.quit()
