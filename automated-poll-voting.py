from selenium import webdriver
import time

url = 'http://www.easypolls.net/poll.html?p=5cb826a3e4b01977b1968d91'
#Opening chrome tab and the url
driver = webdriver.Chrome()
driver.get(url)

#vote 10 times on the selected option and delete the cookies after that@@
for i in range(10):
	driver.get(url)
	driver.find_element_by_xpath('//*[@id="c_2_5cb826a3e4b01977b1968d91"]').click()
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="OPP-poll-vote-button"]').click()
	time.sleep(2)
	driver.delete_all_cookies()
	time.sleep(1)
	driver.refresh()