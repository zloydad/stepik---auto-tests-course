from selenium import webdriver
import math

link = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()
browser.get(link)

text = str(math.ceil(math.pow(math.pi, math.e)*10000))
href = link = browser.find_element_by_link_text(text)
href.click()


input1 = browser.find_element_by_tag_name("input")
input1.send_keys("Evgeniy")
input2 = browser.find_element_by_name("last_name")
input2.send_keys("Sirotenko")
input3 = browser.find_element_by_class_name("city")
input3.send_keys("Saint-Petersburg")
input4 = browser.find_element_by_id("country")
input4.send_keys("Russia")
button = browser.find_element_by_css_selector("button.btn")
button.click()

