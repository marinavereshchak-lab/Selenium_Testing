from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import os
# 1. Инициализация:
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 15)
# 2. Открываем страницу с формой:
driver.get("https://the-internet.herokuapp.com/login")
# 3. Заполняем текстовое поле:
text_input = driver.find_element(By.ID, "username")
text_input.clear()
text_input.send_keys("tomsmith")
# 4. Заполняем поле пароля:
password_input = driver.find_element(By.ID, "password")
password_input.clear()
password_input.send_keys("SuperSecretPassword!")

# 15. Отправляем форму:
submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
submit_button.click()

# 16. Закрываем браузер:
driver.quit()


