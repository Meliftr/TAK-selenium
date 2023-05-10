import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from locator import elem
from data import input

class webshop(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_positiv_register(self):
        driver = self.driver
        driver.get(input.baseURL)
        driver.find_element(By.CLASS_NAME, login_btn).click()
        url = driver.current_url
        self.assertEqual(url, input.baseURL + "login")
        driver.find_element(By.ID, elem.emaillogin).send_keys(input.valid_email)
        driver.find_element(By.ID, elem.passwordlogin).send_keys(input.valid_password)
        driver.find_element(By.ID, elem.radio_remember_btn).click()
        driver.find_element(By.ID, elem.login2_bt).click()
        self.assertNotIn("No results found.", driver.page_source)
        url2 = driver.current_url
        self.assertEqual(url2, baseURL)
        data = driver.find_element(By.CSS_SELECTOR, elem.titlestore).text
        self.assertIn("Welcome to our store")
    
    def test_positiv_register(self):
        driver = self.driver
        driver.get(input.baseURL)
        driver.find_element(By.CLASS_NAME, login_btn).click()
        url = driver.current_url
        self.assertEqual(url, input.baseURL + "login")
        driver.find_element(By.ID, elem.emaillogin).send_keys()
        driver.find_element(By.ID, elem.passwordlogin).send_keys()
        driver.find_element(By.ID, elem.radio_remember_btn).click()
        driver.find_element(By.ID, elem.login2_bt).click()
        data = driver.find_element(By.CSS_SELECTOR, elem.errormsg_login).text
        self.assertIn("Login was unsuccessful. Please correct the errors and try again.")


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()