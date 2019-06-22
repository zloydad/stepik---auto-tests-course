from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_css_selector("[id='input_value']")
x = x_element.text
y = calc(x)

input_name = browser.find_element_by_css_selector("[id='answer']")
input_name.send_keys(y)

checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
checkbox.click()

radio = browser.find_element_by_css_selector("[id='robotsRule']")
radio.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()


