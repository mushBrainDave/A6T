import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class login_test(unittest.TestCase):

    def setUp(self):
       self.driver = webdriver.Chrome()
       self.wait_time = 2
       user = "instructor"
       pwd = "maverick1a"
       self.driver.maximize_window()
       self.driver.get("https://gallant-ardinghelli-0dbec2.netlify.app/")
       elem = self.driver.find_element_by_xpath(
           "/html/body/div[1]/div[3]/div/div/div/div[2]/div/div/div/div/form/div/div[1]/div/div[2]/div[1]/div/input")
       elem.send_keys(user)
       elem = self.driver.find_element_by_xpath(
           "/html/body/div[1]/div[3]/div/div/div/div[2]/div/div/div/div/form/div/div[2]/div/div[2]/div[1]/div[1]/input")
       elem.send_keys(pwd)
       elem = self.driver.find_element_by_xpath(
           "/html/body/div[1]/div[3]/div/div/div/div[2]/div/div/div/div/form/div/div[5]/button").click()
       time.sleep(self.wait_time)

    def test_intake_add(self):
        elem = self.driver.find_element_by_xpath("/html/body/div[1]/div/header/div/div[3]/a[2]/span").click()
        time.sleep(self.wait_time)
        elem = self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div/main/div/div/div[2]/div/button").click()
        time.sleep(self.wait_time)
        elem = self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div/div/div[2]/div/div/div[3]/form/div/div[1]/div/div[1]/div/input")
        elem.send_keys("1987")
        elem = self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div/div/div[2]/div/div/div[3]/form/div/div[2]/div/div[1]/div/input")
        elem.send_keys("150")
        elem = self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div/div/div[2]/div/div/div[3]/form/div/div[3]/div/div[1]/div/input")
        elem.send_keys("20")
        elem = self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div/div/div[2]/div/div/div[3]/form/div/div[4]/div/div[1]/div/input")
        elem.send_keys("30")
        elem = self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div/div/div[2]/div/div/div[3]/form/div/div[5]/div/div[1]/div/input")
        elem.send_keys("30")
        elem = self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div/div/div[2]/div/div/div[3]/form/div/div[6]/div/div[1]/div/input")
        elem.send_keys("30")
        elem = self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div/div/div[2]/div/div/div[3]/form/div/div[7]/div/div[1]/div/input")
        elem.send_keys("10202020")
        time.sleep(self.wait_time)
        elem = self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div/div/div[2]/div/div/div[3]/form/button[1]").click()

    def test_intake_edit(self):
        elem = self.driver.find_element_by_xpath("/html/body/div[1]/div/header/div/div[3]/a[2]/span").click()
        time.sleep(self.wait_time)
        elem = self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div/main/div/div/div[2]/div/main/div/div/div[2]/div[1]/table/tbody/tr[1]/td[8]/button").click()
        elem = self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div/div/div[2]/div/div/div[3]/form/div/div[1]/div/div[1]/div/input")
        elem.send_keys("1987")
        elem = self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div/div/div[2]/div/div/div[3]/form/div/div[2]/div/div[1]/div/input")
        elem.send_keys("150")
        elem = self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div/div/div[2]/div/div/div[3]/form/div/div[3]/div/div[1]/div/input")
        elem.send_keys("20")
        elem = self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div/div/div[2]/div/div/div[3]/form/div/div[4]/div/div[1]/div/input")
        elem.send_keys("30")
        elem = self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div/div/div[2]/div/div/div[3]/form/div/div[5]/div/div[1]/div/input")
        elem.send_keys("30")
        elem = self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div/div/div[2]/div/div/div[3]/form/div/div[6]/div/div[1]/div/input")
        elem.send_keys("30")
        elem = self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div/div/div[2]/div/div/div[3]/form/div/div[7]/div/div[1]/div/input")
        elem.send_keys("10202020")
        elem = self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div/div/div[2]/div/div/div[3]/form/button[1]").click()

    def test_intake_delete(self):
        elem = self.driver.find_element_by_xpath("/html/body/div[1]/div/header/div/div[3]/a[2]/span").click()
        time.sleep(self.wait_time)
        elem = self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div/main/div/div/div[2]/div/main/div/div/div[2]/div[1]/table/tbody/tr[1]/td[9]/button").click()

    def test_settings_edit(self):
        elem = self.driver.find_element_by_xpath("/html/body/div[1]/div/header/div/div[3]/a[3]").click()
        time.sleep(self.wait_time)
        elem = self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div/main/div/div/div[2]/div/div/div[1]/table/tbody/tr/td[9]/button").click()
        time.sleep(self.wait_time)
        elem = self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div/div/div[2]/div/div/div[3]/form/button[1]").click()
        time.sleep(self.wait_time)

    def test_date_range(self):
        elem = self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div/main/div/div[2]/div/div/div[1]/div[2]/div[1]/div/input").click()
        time.sleep(self.wait_time)
        elem = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div[2]/table/tbody/tr[4]/td[3]/button").click()
        elem = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div[2]/table/tbody/tr[5]/td[7]/button").click()
        time.sleep(self.wait_time)

    def tearDown(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/div/header/div/div[3]/button").click()
        self.driver.close()


if __name__ == "__main__":
   unittest.main()