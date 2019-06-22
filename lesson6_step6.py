from selenium import webdriver
import os 
import math

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_css_selector("button.btn-primary")
button.click()

confirm = browser.switch_to.alert
confirm.accept()

x = browser.find_element_by_id("input_value").text

input_name = browser.find_element_by_id("answer")
input_name.send_keys(str(math.log(abs(12*math.sin(int(x))))))

button2 = browser.find_element_by_css_selector("button.btn")
button2.click()









