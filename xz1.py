import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

# Когда ты запустишь код у тебя откроется браузер, после этого в pyCharm в консоли попросят ссылку ("link here")
driver.get(input("link here"))
driver.implicitly_wait(5)

search_box = driver.find_element(By.XPATH, '//*[@id="joinform-gamecode"]')
search_box.send_keys(input('Code here '))

search_box = driver.find_element(By.XPATH, '//*[@id="joinform-name"]')
search_box.send_keys(' ᠌ ᠌ ᠌᠌ ᠌ ᠌ ᠌ ᠌ ᠌ ')

search_button = driver.find_element(By.XPATH, '//*[@id="participate-form-code"]/button')
search_button.click()
time.sleep(10)

search_but = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div')
search_but.click()

search_bu = driver.find_element(By.XPATH, '//*[@id="w0"]/div/div/div[3]/div/a[3]/i')
search_bu.click()

print(driver.current_url)






























# Первая команда ищет поле Введите имя, а вторая ищет кнопу Почати тест или как-то так
#search_box = driver.find_element(By.NAME, "JoinForm[gamecode]")
#search_box = driver.find_element(By.NAME, "JoinForm[name]")
#search_button = driver.find_element(By.TAG_NAME, 'button')



#generate_random_string(8)

# Эта команда означает сделать клик лкм по кнопке которую мы нашли ранее (Почати тест), команда time.sleep заставляет скрипт подождать 5 сек чтобы страница успела прогрузится после ввода имени
#search_button.click()
#time.sleep(5)

# Поскольку если ты просто зайдёшь на тест и нажмёшь крестик тебе не покажут ответы поэтому пришлось искать как нажать на первый попавшийся елемент чтобы сайт дал ответы
#search_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/p')
#search_button.click()
#time.sleep(5)

# Тут мы ищем тот самый крестик который даёт нам доступ к заветным ответам и нажимаем на него
#search_button = driver.find_element(By.CLASS_NAME, 'endSessionButton')
#search_button.click()
#time.sleep(5)

#print(driver.current_url)