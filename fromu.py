# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

driver = webdriver.Firefox()

driver.get("http://localhost/addressbook/")
elementu = driver.find_element(By.NAME,"name")
elementu.click()
elementu.clear()
elementu.send_keys("admin")
elementp = driver.find_element(By.NAME,value="pass")
elementp.click()
elementp.clear()
elementp.send_keys("secret")
driver.find_element(By.XPATH,"//input[@value='Login']").click()
driver.find_element(By.LINK_TEXT,"groups").click()

