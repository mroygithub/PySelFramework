import unittest
import Reusable
from selenium import webdriver
from Reusable.reusable_methods import ReusableTest
from PageObject.Home import HomePage
from Reusable import Driver


class SearchText(unittest.TestCase):

    @staticmethod
    def setUp():
        Driver.Instance.maximize_window()
        Driver.Instance.get(ReusableTest.ReadXMLByNodeName("applicationurl"))

    def test_scenarios_execution(self):
        # get the search textbox
        self.assertTrue(self.driver.find_element_by_xpath(HomePage.applicationLogo()))

    @classmethod
    def tearDown(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
