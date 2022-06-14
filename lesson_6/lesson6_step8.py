from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

#* говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 20).until(
EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
browser.find_element(by = By.ID, value = "book").click()

input_text = browser.find_element(by = By.ID, value = "input_value").text

input_name = browser.find_element(by = By.ID, value = "answer")
input_name.send_keys(str(math.log(abs(12*math.sin(int(input_text))))))

solve = browser.find_element(by = By.CSS_SELECTOR, value = "button#solve")
solve.click()
#* Получаем ответ из alert
alert = browser.switch_to.alert
alertText = alert.text
alert.accept()

browser.close()
#* Парсим ответ и выводим
list = alertText.split()
x = 0
for i in list:
    x = x + 1

print(list[x-1])
