from selenium                           import webdriver

from selenium.webdriver.support.ui      import WebDriverWait

from selenium.webdriver.common.by       import By

from selenium.webdriver.support.select  import Select

import unittest

import time


class GetTextOrAttribute(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("http://www.changethissite.com")
        driver.maximize_window()
     
    def test_GetTextOrAttribute(self):
        seePhotosButtonLocator = "(//span[@class='wsite-button-inner'])[1]"
        seePhotosButtonElement = WebDriverWait(driver, 10).\
                                 until(lambda driver: driver.find_element_by_xpath(seePhotosButtonLocator))
        text = seePhotosButtonElement.text
        print text
        classAttribute = seePhotosButtonElement.get_attribute("class")
        print classAttribute
        
    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()



