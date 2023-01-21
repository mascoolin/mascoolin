import imp
from lib2to3.pgen2 import driver
import unittest
import time
from urllib import response
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class MySignUP (unittest.TestCase):

    def setUp(self) :
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_login_positif(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()
        driver.get("https://www.saucedemo.com/inventory.html")
        driver.find_element(By.NAME,"product_sort_container")
        driver = Select(dropdown)
        driver.select_by_index(1)
        time.sleep(3)

    def test_login_negatif(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard")
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret")
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()

        response_message = driver.find_element(By.CSS_SELECTOR, "#login-button_container > div > form > div.error-message-container.error >h3").text
        self.assertEqual(response_message, 'Epic sadface: Username and password do not match any user in this service')

    def test_sign_up(self):
        driver=self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.find_element(By.ID,"signUp").click()
        time.sleep(3)
        driver.implicitly_wait(30)
        driver.find_element(By.ID,"name-register").send_keys("Standar")
        time.sleep(3)
        driver.implicitly_wait(30)
        email = driver.find_element(By.ID,"email-register").send_keys("adaajacobaan@gmail.com")
        email.clear()
        time.sleep(3)
        driver.implicitly_wait(30)
        password = driver.find_element(By.ID,"password-register").send_keys("secretsaja")
        password.clear()
        time.sleep(3)
        driver.find_element(By.ID,"signup-register").click()

    def tearDown(self):
        self.driver.close()

unittest.main()