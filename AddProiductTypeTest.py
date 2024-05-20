import unittest

from parameterized import parameterized

from steps.ReadDataTest import readDataTest
from steps.Step_add_product_type import stepAddProductType
from utils.CustomChromeDriver import customChrome
from verifys.Verify_add_product_type import verifyAddProductType

dataTests = readDataTest().data_test("dataTest/data_test_add_product_type.xlsx")


class MyTestCase(unittest.TestCase):

    def setUp(self):
        print("==== [Begin Test] ====")
        self.browser = customChrome()
        self.browser.get("http://localhost:3000/productType/-1")

    def tearDown(self):
        self.browser.quit()
        print("==== [End Test] ====")

    @parameterized.expand(dataTests)
    def test_add_product_type(self, no, name, brand, time, quantity, position, message, validate_name, validate_ncc, validate_time,	validate_quantity):
        stepAddProductType(self.browser).add_product(name, brand, time, quantity, position)
        self.assertEqual(message, verifyAddProductType(self.browser).getMessage())  # add assertion here
        self.assertEqual(validate_name, verifyAddProductType(self.browser).validate_name())
        self.assertEqual(validate_ncc, verifyAddProductType(self.browser).validate_ncc())
        self.assertEqual(validate_time, verifyAddProductType(self.browser).validate_time())
        self.assertEqual(validate_quantity, verifyAddProductType(self.browser).validate_quantity())


if __name__ == '__main__':
    unittest.main()
