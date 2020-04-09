# Python program to demonstrate  
# use of class method and static method.

from Reusable import Driver
from PageObject.Home import HomePage
from datetime import date 


class HomeTestDef:

    @staticmethod
    def GoToURL(url):
        Driver.Instance.maximize_window()
        Driver.Instance.get(url)

    @staticmethod
    def header_options_validation(self):
        try:
            self.assertTrue(Driver.is_web_element_displayed(HomePage.applicationLogo()))
            Driver.click_and_implicit_wait(HomePage.loginLink())
            Driver.go_back(5)
            print("PAss")

        except:
            print("Fail")

    @staticmethod
    def footer_options_validation(self):
        try:
            self.assertTrue(Driver.is_web_element_displayed(HomePage.applicationLogo()))
            Driver.click_and_implicit_wait(HomePage.loginLink())
            Driver.go_back(5)
            print("Pass")

        except:
            print("Fail")
