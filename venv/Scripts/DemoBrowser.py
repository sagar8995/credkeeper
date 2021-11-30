from selenium import webdriver

# browser exposes an executable file
# through selenium test  we need to invoke the executable file which will then invoke actual browser.

driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")

driver.get("https://nebo.mcstaging.acgbrands.com/en_US/index.php/") #get method to hit  url on browser

driver.maximize_window()

print(driver.title)

print(driver.current_url)

driver.get("https://nebo.mcstaging.acgbrands.com/en_US/egk-16w-warm-white-wall-led-spot-light.html")

driver.find_element_by_xpath("//body/div[2]/main[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/button[1]").click()

#driver.minimize_window()

#driver.back()
#driver.refresh()

#driver.close()
#driver.quit()

