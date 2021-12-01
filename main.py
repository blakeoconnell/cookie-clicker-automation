from selenium import webdriver

chrome_driver_path = "C:/Users/bmoco/Downloads/chromedriver_win32/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
driver.maximize_window()
event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")

for time in event_times:
    print(time.text)

for name in event_names:
    print(name.text)

upcoming_events = {}

for index in range(len(event_names)):
    upcoming_events[index] = {'time': event_times[index].text, 'name': event_names[index].text}

print(upcoming_events)
driver.quit()