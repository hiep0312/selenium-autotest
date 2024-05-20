import time
from csv import excel

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.Add_staff_page import msg_result, validation_name, validation_phone, validation_email, validation_address, \
    validation_username, validation_password, validation_work_start_time, validation_position


class verifyAddStaff:
    def __init__(self, driver):
        self.driver = driver

    def waitAddFinish(self):
        return WebDriverWait(self.driver, 3).until()
        # .until(EC.presence_of_element_located((By.CLASS_NAME, msg_result()))))

    def add_staff(self):
        # self.waitAddFinish()
        time.sleep(1)
        content = self.driver.find_element(By.CLASS_NAME, msg_result()).text
        return content

    def get_name(self):
        try:
            content = self.driver.find_element(By.CLASS_NAME, validation_name()).text
        except:
            content = ""
        return content

    def get_phone(self):
        try:
            content = self.driver.find_element(By.CLASS_NAME, validation_phone()).text
        except:
            content = ""
        return content

    def get_email(self):
        try:
            content = self.driver.find_element(By.CLASS_NAME, validation_email()).text
        except:
            content = ""
        return content

    def get_address(self):
        try:
            content = self.driver.find_element(By.CLASS_NAME, validation_address()).text
        except:
            content = ""
        return content

    def get_position(self):
        try:
            content = self.driver.find_element(By.CLASS_NAME, validation_position()).text
        except:
            content = ""
        return content

    def get_username(self):
        try:
            content = self.driver.find_element(By.CLASS_NAME, validation_username()).text
        except:
            content = ""
        return content

    def get_password(self):
        try:
            content = self.driver.find_element(By.CLASS_NAME, validation_password()).text
        except:
            content = ""
        return content

    def get_time(self):
        try:
            content = self.driver.find_element(By.CLASS_NAME, validation_work_start_time()).text
        except:
            content = ""
        return content
