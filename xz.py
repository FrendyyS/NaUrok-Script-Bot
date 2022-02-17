import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()



driver.get(input("link here"))
driver.implicitly_wait(5)


search_box = driver.find_element(By.NAME, "SessionForm[firstname]")
search_button = driver.find_element(By.TAG_NAME, 'button')

search_box.send_keys("Zaza")

search_button.click()
time.sleep(5)


search_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/p')
search_button.click()
time.sleep(5)




search_button = driver.find_element(By.CLASS_NAME, 'endSessionButton')
search_button.click()

