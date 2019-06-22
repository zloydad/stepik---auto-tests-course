from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_tag_name("img")
x = x_element.get_attribute("valuex")
y = calc(x)

input_name = browser.find_element_by_css_selector("[id='answer']")
input_name.send_keys(y)

checkbox = browser.find_element_by_id("robotCheckbox")
checkbox.click()

radio = browser.find_element_by_css_selector("[id='robotsRule']")
radio.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()


