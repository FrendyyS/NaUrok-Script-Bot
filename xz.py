import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


# Когда ты запустишь код у тебя откроется браузер, после этого в pyCharm в консоли попросят ссылку ("link here")
driver.get(input("link here"))
driver.implicitly_wait(5)

# Первая команда ищет поле Введите имя, а вторая ищет кнопу Почати тест или как-то так
search_box = driver.find_element(By.NAME, "SessionForm[firstname]")
search_button = driver.find_element(By.TAG_NAME, 'button')

# Эта команда вводит рандомный набор букв(точнее ьудет вводить после того как ты найдёшь как это сделать ;) )
search_box.send_keys("Zaza")

# Эта команда означает сделать клик лкм по кнопке которую мы нашли ранее (Почати тест), команда time.sleep заставляет скрипт подождать 5 сек чтобы страница успела прогрузится после ввода имени
search_button.click()
time.sleep(5)

# Поскольку если ты просто зайдёшь на тест и нажмёшь крестик тебе не покажут ответы поэтому пришлось искать как нажать на первый попавшийся елемент чтобы сайт дал ответы
search_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/p')
search_button.click()
time.sleep(5)



# Тут мы ищем тот самый крестик который даёт нам доступ к заветным ответам и нажимаем на него
search_button = driver.find_element(By.CLASS_NAME, 'endSessionButton')
search_button.click()

