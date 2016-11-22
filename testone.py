from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest
class Test_PythonOrg(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("c:\Python27\chromedriver")
        strBrowser=self.browser
        return strBrowser
    def tearDown(self):
        sleep(4)
        self.browser.close()
        self.browser = None
    def test_00_SearchBoxWorks(self):
        "Test to make sure that the search box works fine."
        self.browser.get("http://www.ebay.co.uk")
        search_entry = self.browser.find_element_by_name("_nkw")
        search_entry.clear()
        search_entry.send_keys("iphone")
        search_entry.send_keys(Keys.RETURN)
        # self.assertTrue("0 results for" not in self.browser.page_source)
    def test_01_clicksigin(strBrowser):
            "Test to make sure that the search box works fine."
            strBrowser.browser.get("http://www.ebay.co.uk")
            link = strBrowser.browser.find_element_by_link_text('Sign in')
            link.click()


if __name__ == "__main__":
    unittest.main(verbosity=2)

