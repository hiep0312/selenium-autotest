import time

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.Add_product_type_page import msg_result


class verifyAddProductType:
    def __init__(self, driver):
        self.driver = driver

    def waitAddFinish(self):
        return WebDriverWait(self.driver, 3).until()
        # .until(EC.presence_of_element_located((By.CLASS_NAME, msg_result()))))

    def getMessage(self):
        # self.waitAddFinish()
        time.sleep(1)
        content = self.driver.find_element(By.CLASS_NAME, msg_result()).text
        return content

    def validate_quantity(self):
        time.sleep(1)
        content = self.driver.find_element(By.CLASS_NAME, ).text
        return content

    def validate_time(self):
        pass

    def validate_ncc(self):
        pass

    def validate_name(self):
        pass
