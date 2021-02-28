from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Firefox()
driver.get('https://app.tennisvenues.com.au/secure/booking/request?v=david-turbayne-tennis-centre&id=C3&d=20210304&t=2000&cm=true')

time.sleep(5)

name = driver.find_element_by_name('name')
name.send_keys('Angus')

bookingTimeRadio = Select(driver.find_element_by_id('endTime'))
bookingTimeRadio.select_by_value('2130')

contactNumber = driver.find_element_by_name('contactNumber')
contactNumber.send_keys('0403779594')

email = driver.find_element_by_name('email')
email.send_keys('anguscheng389@gmail.com')


confirmEmail = driver.find_element_by_name('confirmEmail')
confirmEmail.send_keys('anguscheng389@gmail.com')

nextButton = driver.find_element_by_id('submit_button')
nextButton.click()

while True:
    time.sleep(420)
    driver.refresh()
