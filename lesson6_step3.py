from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

x = browser.find_element_by_id("num1").text
y = browser.find_element_by_id("num2").text

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(int(x)+int(y)))

button = browser.find_element_by_css_selector("button.btn")
button.click()









