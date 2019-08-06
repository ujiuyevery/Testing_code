import unittest
from selenium import webdriver
import time
class YouJiuYe(unittest.TestCase):

    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.get("http://xue.ujiuye.com/foreuser/login/")

    def test_login_password(self):
        username_dl = self.chrome.find_element_by_id("username_dl")
        password_dl = self.chrome.find_element_by_id("password_dl")
        button = self.chrome.find_element_by_class_name("loginbutton1")

        username_dl.send_keys("13012012345")
        password_dl.send_keys("123")

        button.click()

        text = self.chrome.find_element_by_id("J_usernameTip").text

        self.assertEqual("密码应该为6-20位之间",text)

        #密码应该为6-20位之间！
    def tearDown(self):
        time.sleep(10)
        self.chrome.close()

if __name__ == '__main__':
    if __name__ == '__main__':
        unittest.main()
