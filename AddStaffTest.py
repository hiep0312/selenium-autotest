import unittest

from parameterized import parameterized
from steps.Step_add_staff import stepAddStaff
from steps.ReadDataTest import readDataTest
from utils.CustomChromeDriver import customChrome
from verifys.Verify_add_staff import verifyAddStaff

dataTests = readDataTest().data_test("dataTest/data_test_add_staff.xlsx")


class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("==== [Begin Test] ====")
        self.browser = customChrome()
        self.browser.get("http://localhost:3000/employee/-1")

    def tearDown(self):
        self.browser.quit()
        print("==== [End Test] ====")

    @parameterized.expand(dataTests)
    def test_add_staff(self, no, name, phone, email, address, position, username, password, work_start_time, message,
                       validate_name, validate_phone, validate_email, validate_address, validate_position,
                       validate_username, validate_password, validate_work_start_time):
        stepAddStaff(self.browser).add_staff(name, phone, email, address, position, username, password, work_start_time)
        print(message, verifyAddStaff(self.browser).add_staff())
        self.assertIn(message, verifyAddStaff(self.browser).add_staff())
        self.assertIn(validate_name, verifyAddStaff(self.browser).get_name())
        self.assertIn(validate_phone, verifyAddStaff(self.browser).get_phone())
        self.assertIn(validate_email, verifyAddStaff(self.browser).get_email())
        self.assertIn(validate_address, verifyAddStaff(self.browser).get_address())
        self.assertIn(validate_position, verifyAddStaff(self.browser).get_position())
        self.assertIn(validate_username, verifyAddStaff(self.browser).get_username())
        self.assertIn(validate_password, verifyAddStaff(self.browser).get_password())
        self.assertIn(validate_work_start_time, verifyAddStaff(self.browser).get_time())


if __name__ == '__main__':
    unittest.main()
