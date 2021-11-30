import time
import logging
from selenium import webdriver
import selenium




driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")

driver.maximize_window()

driver.get("https://dev2.thebest.directory/admin/")

driver.find_element_by_name("email").send_keys("testing.admindev2@yopmail.com")

driver.find_element_by_name("password").send_keys("Bytes@123")

driver.find_element_by_xpath("//button[contains(text(),'Login')]").click()

#driver.execute_script('''window.open("https://yopmail.com/en/wm", "_blank");''')

###driver.get("https://yopmail.com/en/wm")

time.sleep(5)

driver.find_element_by_xpath("//body/app-root[1]/div[1]/app-navbar[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]").click()


#driver.find_element_by_id("https://dev2.thebest.directory/admin/admin-article-list")
#driver.find_element_by_xpath("//a[@id='https://dev2.thebest.directory/admin/admin-article-list']")
#driver.find_element_by_link_text("Article")
#element.click()
driver.find_element_by_name("search").send_keys("test")

time.sleep(5)

driver.find_element_by_id("category").send_keys("CSM")

driver.find_element_by_id("autoshare").send_keys("Yes")

driver.find_element_by_class_name("ngx-dropdown-button").click()

obj = select(driver.find_element_by_name("search-text").send_keys("Sagar Soni"))
obj.select_by_visible_text(" Sagar Soni ")



# time.sleep(4)
# element.click()

driver.find_element_by_id("articleStatus").send_keys(" Approve To Article Staging ")

driver.find_element_by_id("dummy_date").send_keys("Last 3 days")




# dropdown.select_by_visible_text("CSM")
# dropdown.select-by_index(1)




#driver.find_elements_by_id("category").send_keys("CSM")





#dropdown.select_by_visible-text("PSRE")



#dropdown.select_by_index(0)
#dropdown.select-by_value( "PSRE")










