import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Blog_ATS(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
       user = "instructor"
       pwd = "maverick1a"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://localhost:8080/auth")
       elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div[2]/div/div/div/div/form/div/div[1]/div/div[2]/div[1]/div/input")
       elem.send_keys(user)
       elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div[2]/div/div/div/div/form/div/div[2]/div/div[2]/div[1]/div[1]/input")
       elem.send_keys(pwd)
       elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div[2]/div/div/div/div/form/div/div[5]/button").click()
       time.sleep(1)

       driver.get("http://localhost:8080/")
       assert (driver.find_element_by_xpath("/html/body/div[1]/div/header/div/div[3]/button/span"))
       elem = driver.find_element_by_xpath("/html/body/div[1]/div/header/div/div[3]/a[2]/span").click()
       time.sleep(5)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()