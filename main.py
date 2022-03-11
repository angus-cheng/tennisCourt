from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# BASE_URL = "https://www.tennisvenues.com.au/booking/david-turbayne-tennis-centre#"
BASE_URL = "https://www.tennisvenues.com.au/booking/morningside-tc#"
# BASE_URL = "http://www.tennisvenues.com.au/booking/wynnum-tennis-centre#"


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(BASE_URL)

    while driver.current_url == BASE_URL:
        pass

    time.sleep(10)

    name = driver.find_element(By.NAME, 'name')
    name.send_keys('Angus')

    contactNumber = driver.find_element(By.NAME, 'contactNumber')
    contactNumber.send_keys('0403779594')

    email = driver.find_element(By.NAME, 'email')
    email.send_keys('anguscheng389@gmail.com')

    confirmEmail = driver.find_element(By.NAME, 'confirmEmail')
    confirmEmail.send_keys('anguscheng389@gmail.com')

    nextButton = driver.find_element(By.ID, 'submit_button')
    nextButton.click()

    while True:
        time.sleep(420)
        driver.refresh()

    return


if __name__ == "__main__":
    main()
