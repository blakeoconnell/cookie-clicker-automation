from selenium import webdriver
import time

chrome_driver_path = "C:/Users/bmoco/Downloads/chromedriver_win32/chromedriver.exe"

COOKIE_CLICKER_URL = "http://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(COOKIE_CLICKER_URL)

driver.maximize_window()

cookie = driver.find_element_by_id("cookie")
shop = driver.find_elements_by_css_selector("div#store b")

timeout = time.time() + 60*5   # 5 minutes from now

while time.time() < timeout:
    second_timer = time.time() + 5
    while time.time() < second_timer:
        cookie.click()
    for index in range(len(shop) - 1, 0, -1):
        money = int(driver.find_element_by_id("money").text)
        shop = driver.find_elements_by_css_selector("div#store b")
        shop.remove(shop[-1])
        shop_prices = [int(item.text.split(" - ")[1].replace(",", "")) for item in shop]
        if money > shop_prices[index]:
            print(f"money: {money}, shop price: {shop_prices[index]}, item: {shop[index].text}")
            shop[index].click()
