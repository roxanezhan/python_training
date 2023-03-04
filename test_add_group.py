# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to().alert
        return True
    except:
        return False

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)

    def test_add_group(self):
        wd = self.wd
        # open home page
        wd.get("http://localhost/addressbook/")
        # login
        wd.find_element(By.NAME,"user").click()
        wd.find_element(By.NAME,"user").clear()
        wd.find_element(By.NAME,"user").send_keys("admin")
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME,"pass").clear()
        wd.find_element(By.NAME,"pass").send_keys("secret")
        wd.find_element(By.XPATH,"//input[@value='Login']").click()
        # open goups page
        wd.find_element(By.LINK_TEXT,"groups").click()
        # init group createion
        wd.find_element(By.NAME,"new").click()
        # fill group form
        wd.find_element(By.NAME,"group_name").click()
        wd.find_element(By.NAME,"group_name").clear()
        wd.find_element(By.NAME,"group_name").send_keys("testgroup")
        wd.find_element(By.NAME,"group_header").click()
        wd.find_element(By.NAME,"group_header").clear()
        wd.find_element(By.NAME,"group_header").send_keys("testheader")
        wd.find_element(By.NAME,"group_footer").click()
        wd.find_element(By.NAME,"group_footer").clear()
        wd.find_element(By.NAME,"group_footer").send_keys("testfooter")
        # submit group createion
        wd.find_element(By.NAME,"submit").click()
        # return to groups page
        wd.find_element(By.LINK_TEXT,"group page").click()
        # logout
        wd.find_element(By.LINK_TEXT,"Logout").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
