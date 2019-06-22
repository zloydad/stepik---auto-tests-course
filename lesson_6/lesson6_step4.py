from selenium import webdriver
import math

link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x = browser.find_element_by_id("input_value").text

input_name = browser.find_element_by_id("answer")
input_name.send_keys(str(math.log(abs(12*math.sin(int(x))))))

checkbox = browser.find_element_by_id("robotCheckbox")
checkbox.click()

button = browser.find_element_by_css_selector("button.btn")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

radio = browser.find_element_by_id("robotsRule")
radio.click()

button.click()









