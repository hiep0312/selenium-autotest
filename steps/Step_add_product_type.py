from selenium.webdriver.common.by import By

from pages.Add_product_type_page import txt_name, txt_brand, txt_time, txt_quantity, txt_position


class stepAddProductType:
    def __init__(self, driver):
        self.driver = driver

    def add_product(self, name, brand, time, quantity, position):
        print("[Step] add_product")
        self.inputName(name)
        self.inputBrand(brand)
        self.inputTime(time)
        self.inputQuantity(quantity)
        self.inputPosition(position)
        self.clickAdd()

    def inputName(self, name):
        print("[+] Input name", name, sep=": ")
        self.get_txtName().clear()
        self.get_txtName().send_keys(name)

    def inputBrand(self, brand):
        print("[+] Input brand", brand, sep=": ")
        self.get_txtBrand().clear()
        self.get_txtBrand().send_keys(brand)

    def inputTime(self, time):
        print("[+] Input time", time, sep=": ")
        self.get_txtTime().clear()
        self.get_txtTime().send_keys(time)

    def inputQuantity(self, quantity):
        print("[+] Input quantity", quantity, sep=": ")
        self.get_txtQuantity().clear()
        self.get_txtQuantity().send_keys(quantity)

    def inputPosition(self, position):
        print("[+] Input position", position, sep=": ")
        self.get_txtPosition().clear()
        self.get_txtPosition().send_keys(position)

    def clickAdd(self):
        print("[+] Click Add")
        self.get_btnAdd().click()

    def get_txtName(self):
        return self.driver.find_element(By.XPATH, txt_name())

    def get_txtBrand(self):
        return self.driver.find_element(By.XPATH, txt_brand())

    def get_txtTime(self):
        return self.driver.find_element(By.XPATH, txt_time())

    def get_txtQuantity(self):
        return self.driver.find_element(By.XPATH, txt_quantity())

    def get_txtPosition(self):
        return self.driver.find_element(By.XPATH, txt_position())
