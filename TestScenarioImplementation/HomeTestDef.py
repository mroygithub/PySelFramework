# Python program to demonstrate  
# use of class method and static method.

from Reusable import Driver
from PageObject.Home import HomePage
from Reusable.reusable_methods import ReusableTest


class HomeTestDef:

    @staticmethod
    def go_to_url(url):

        Driver.Instance.maximize_window()
        Driver.Instance.get(url)

    @staticmethod
    def header_options_validation(self, html_report):
        try:
            self.assertTrue(Driver.is_web_element_displayed(HomePage.applicationLogo()))
            Driver.click_and_implicit_wait(HomePage.loginLink())
            Driver.go_back(5)
            print("PAss")
            ReusableTest.when_test_is_pass(html_report, "TC-001", "Home Page Logo is available")
            ReusableTest.when_test_is_pass(html_report, "TC-001", "Home Page Sign In is available")

        except:
            print("Fail")

    @staticmethod
    def footer_options_validation(self, htmlreport):
        try:
            self.assertTrue(Driver.is_web_element_displayed(HomePage.applicationLogo()))
            Driver.click_and_implicit_wait(HomePage.loginLink())
            Driver.go_back(5)
            print("Pass")
            ReusableTest.when_test_is_pass(htmlreport, "TC-001", "Home Page Logo is available")
            ReusableTest.when_test_is_pass(htmlreport, "TC-001", "Home Page Sign In is available")

        except:
            print("Fail")
