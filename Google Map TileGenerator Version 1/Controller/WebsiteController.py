from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import requests
from requests import request
import urllib3
import time
import os


class SeliumWebsiteController:
    def __init__(self, full_screen=False):
        urllib3.disable_warnings()
        self.driver = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
        if full_screen:
            self.driver.maximize_window()

    def ReturnWebpage(self, webpage_url=None, sleep=1, use_soup=True):
        if not webpage_url is None:
            self.driver.get(webpage_url)
        time.sleep(sleep)
        if use_soup:
            return BeautifulSoup(self.driver.page_source, "html.parser")
        else:
            return self.driver.page_source


    def PressButton(self, class_name=None, id_name=None):
        if not class_name is None:
            self.driver.find_element(By.CLASS_NAME, class_name).click()
        elif not id_name is None:
            self.driver.find_element(By.ID, id_name).click()

    def ClearInputField(self, class_name=None, id_name=None):
        if not class_name is None:
            self.driver.find_element(By.CLASS_NAME, class_name).clear()
        elif not id_name is None:
            self.driver.find_element(By.ID, id_name).clear()

    def EnterInputField(self, value, class_name=None, id_name=None):
        if not class_name is None:
            self.driver.find_element(By.CLASS_NAME, class_name).send_keys(value)
        elif not id_name is None:
            self.driver.find_element(By.ID, id_name).send_keys(value)

    def ScrollWebpage(self, y_amount, sleep=1):
        self.driver.execute_script(f"window.scroll(0, {y_amount})")
        time.sleep(sleep)

    def LoginTOGoogle(self):
        self.driver.get("https://accounts.google.com/signin")

