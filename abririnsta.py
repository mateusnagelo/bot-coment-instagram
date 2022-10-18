from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from playwright.sync_api import sync_playwright
import time
import random

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r'C:\WebDrivers\geckodriver.exe', options = options)



    def login(self):
            driver = self.driver
            driver.get("https://www.instagram.com")
            time.sleep(8)
    
            login_button.click()
            time.sleep(3)
            user_element = driver.find_element_by_xpath(
                '//*[@id="loginForm"]/div/div[1]/div/label/input')
            user_element.clear()
            user_element.send_keys(self.username)
            time.sleep(3)
            password_element = driver.find_element_by_xpath(
                "//input[@name='informatica013']")
            password_element.clear()
            password_element.send_keys(self.password)
            time.sleep(3)
            password_element.send_keys(Keys.RETURN)
            time.sleep(5) 
        
            login_button = driver.find_element_by_xpath(
            "//a[@href='/accounts/login/?source=auth_switcher']"
        )
        
            
            
mateusBot = InstagramBot('imports_bjl','informatica013')  
mateusBot.login()  




