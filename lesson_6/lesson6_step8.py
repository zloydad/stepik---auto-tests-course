from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 12).until(
EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR"))
browser.find_element_by_id("book").click()

x = browser.find_element_by_id("input_value").text

input_name = browser.find_element_by_id("answer")
input_name.send_keys(str(math.log(abs(12*math.sin(int(x))))))

solve = browser.find_element_by_css_selector("button#solve")
solve.click()









