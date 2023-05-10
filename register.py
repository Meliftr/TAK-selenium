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
        driver.find_element(By.CLASS_NAME, elem.regis_btn).click()
        url = driver.current_url
        self.assertEqual(url, input.baseURL + "register")
        driver.find_element(By.ID, elem.radio_female_btn).click()
        driver.find_element(By.ID, elem.fname).send_keys(input.valid_fname)
        driver.find_element(By.ID, elem.lsaname).send_keys(input.valid_lname)
        driver.find_element(By.ID, elem.email).send_keys(input.valid_email)
        driver.find_element(By.ID, elem.password).send_keys(input.valid_password)
        driver.find_element(By.ID, elem.cpassword).send_keys(input.valid_cpassword)
        driver.find_element(By.ID, elem.regis2_btn).click()
        self.assertNotIn("No results found.", driver.page_source)
        url2 = driver.current_url
        self.assertEqual(url2, baseURL + "registerresult/1")
        data = driver.find_element(By.CSS_SELECTOR, elem.titlewolcome).text
        self.assertIn("Welcome, Please Sign In!")
    
    def test_negativ_register(self):
        driver = self.driver
        driver.get(input.baseURL)
        driver.find_element(By.CLASS_NAME, elem.regis_btn).click()
        url = driver.current_url
        self.assertEqual(url, input.baseURL + "register")
        driver.find_element(By.ID, elem.radio_female_btn).click()
        driver.find_element(By.ID, elem.fname).send_keys(input.valid_fname)
        driver.find_element(By.ID, elem.lsaname).send_keys(input.valid_lname)
        driver.find_element(By.ID, elem.email).send_keys(input.valid_email)
        driver.find_element(By.ID, elem.password).send_keys(input.valid_password)
        driver.find_element(By.ID, elem.cpassword).send_keys()
        driver.find_element(By.ID, elem.regis2_btn).click()
        data = driver.find_element(By.ID, elem.errormsg_regis).text
        self.assertIn("Password is required.")


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()