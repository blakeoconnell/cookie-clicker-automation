from selenium import webdriver

chrome_driver_path = "C:/Users/bmoco/Downloads/chromedriver_win32/chromedriver.exe"

WIKI_URL = "http://secure-retreat-92358.herokuapp.com/"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(WIKI_URL)
first_name_field = driver.find_element_by_name("fName")
last_name_field = driver.find_element_by_name("lName")
email_field = driver.find_element_by_name("email")
signup_button = driver.find_element_by_class_name("btn")

first_name_field.send_keys("Blake")
last_name_field.send_keys("O'Connell")
email_field.send_keys("blake.mw.oconnell@gmail.com")
signup_button.click()


# driver.quit()