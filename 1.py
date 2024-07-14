2
3
4
5
6
7
8
9
10
11
12
13

from selenium import webdriver

# Указываем путь к драйверу Chrome
driver = webdriver.Chrome(executable_path='D:\PYTON\Project10_Selenium\1.py')

# Открываем страницу Google
driver.get("https://www.google.com")

# Проверяем, что заголовок страницы соответствует ожидаемому
assert driver.title == "Google"

# Закрываем браузер
driver.quit()