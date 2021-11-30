import time
import logging
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")

driver.maximize_window()
driver.get("https://www.wazofurniture.com/") #get method to hit  url on browser

#time.sleep(2000)
#driver.find_element_by_css_selector("svg[fill='none']").click()
#driver.find_element_by_css_selector("button[data-action='close-popup']").click()

time.sleep(10)

#driver.find_element_by_xpath("//body[@data-visualcompletion ='ignore']")

#driver.find_element_by_css_selector("a[class='Heading u-h6']")
driver.find_element_by_css_selector("input[name='contact[email]']").send_keys("Sagar")  # working

driver.find_element_by_css_selector("button[class='NewsletterPopup__Close']").click()

driver.find_element_by_xpath("//body/div[6]/main[1]/div[4]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/img[1]").click()

time.sleep(3)

driver.find_element_by_xpath("//label[contains(text(),'210cm')]").click()

time.sleep(3)

#driver.find_element_by_xpath("//body[1]/div[6]/main[1]/div[1]/section[1]/div[1]/div[3]/div[1]/div[1]/form[1]/div[1]/div[3]/div[1]/input[1]").click()  # count click event

driver.find_element_by_xpath("//body[1]/div[6]/main[1]/div[1]/section[1]/div[1]/div[3]/div[1]/div[1]/form[1]/div[1]/div[3]/div[1]/span[2]").click()

time.sleep(3)

#driver.find_element_by_xpath("//body[1]/div[6]/main[1]/div[1]/section[1]/div[1]/div[3]/div[1]/div[1]/form[1]/div[1]/div[3]/div[1]/input[1]").send_keys(10)

time.sleep(3)

driver.find_element_by_xpath("//body[1]/div[6]/main[1]/div[1]/section[1]/div[1]/div[3]/div[1]/div[1]/form[1]/button[1]").click()





#driver.find_element_by_xpath("").click()

#driver.find_element_by_id("newsletter-popup").send_keys("makwanasagar@gmail.com")

