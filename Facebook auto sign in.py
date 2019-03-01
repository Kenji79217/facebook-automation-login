from selenium import webdriver
import time

path = '/Users/xxxxxx/Desktop/chromedriver/chromedriver'

driver = webdriver.Chrome(path)

driver.get('https://www.facebook.com/')
print(driver.current_url)
print(driver.title)
driver.refresh()

#email
driver.find_element_by_xpath('//*[@id="email"]').send_keys('user account')

#password
driver.find_element_by_xpath('//*[@id="pass"]').send_keys('user password')

#button
driver.find_element_by_xpath('//*[@id="u_0_2"]').click()
time.sleep(30)

driver.close()
driver.quit()




