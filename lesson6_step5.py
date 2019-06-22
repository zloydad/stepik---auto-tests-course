from selenium import webdriver
import os 

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'text.txt')           # добавляем к этому пути имя файла 

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

input_name = browser.find_element_by_name("firstname")
input_name.send_keys("Popka")

input_last = browser.find_element_by_name("lastname")
input_last.send_keys("Durak")

input_email = browser.find_element_by_name("email")
input_email.send_keys("@mail.ru")

input_email = browser.find_element_by_id("file")
input_email.send_keys(file_path)

button = browser.find_element_by_css_selector("button.btn")
button.click()









