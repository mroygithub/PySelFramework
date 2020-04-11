# Python program to demonstrate  
# use of class method and static method.

from Reusable import Driver
from PageObject.SignIn import SignInPage
from PageObject.Home import HomePage
from Reusable.reusable_methods import ReusableTest


class SignInTestDef:

    @staticmethod
    def go_to_url(url):

        Driver.Instance.maximize_window()
        Driver.Instance.get(url)

    @staticmethod
    def sign_in_header(self, html_report):
        try:
            Driver.click_and_implicit_wait(HomePage.loginLink())
            self.assertTrue(Driver.is_web_element_displayed(SignInPage.sign_in_page_header()))
            self.assertEquals("Please Sign In to Continue", Driver.get_element_text(SignInPage.sign_in_page_title()))
            ReusableTest.when_test_is_pass(html_report, "SignIn-TC-001", "Sign In Page Header is available")
            ReusableTest.when_test_is_pass(html_report, "SignIn-TC-002", "Please Sign In to Continue is available")

        except:

            ReusableTest.when_test_is_fail(html_report, "SignIn-TC-001", "Sign In Page Header is not available")
            ReusableTest.when_test_is_fail(html_report, "SignIn-TC-002", "Please Sign In to Continue is not available")

    @staticmethod
    def sign_in_body(self, html_report):
        try:
            Driver.click_and_explicit_wait(SignInPage.submit_log_in(), 5)
            self.assertTrue(Driver.is_web_element_displayed(SignInPage.email_error()))
            ReusableTest.when_test_is_pass(html_report, "SignIn-TC-003", "User is getting error with wrong id/pw login")

        except:
            ReusableTest.when_test_is_fail(html_report, "SignIn-TC-003", "User is not getting error with wrong id/pw login")
