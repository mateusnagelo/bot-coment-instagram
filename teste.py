from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import random

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path=r'C:\WebDrivers\geckodriver.exe', options=options)

# driver.get('https://www.instagram.com')

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
        # self.driver = webdriver.Firefox(executable_path=r'C:\projetos\IGBOT\geckodriver.exe')
       


        def login(self):
            driver = self.driver
            driver.get("https://www.instagram.com")
            
mateusBot = InstagramBot('Issovaidominaromundo','aindabemqueeuseicriarum')  
mateusBot.login()          
         