from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.cntraveller.in/")
# to fire up a new tab using javascript and load google.com
driver.execute_script('''window.open("https://www.google.com", "_blank");''')
time.sleep(5)
driver.quit()