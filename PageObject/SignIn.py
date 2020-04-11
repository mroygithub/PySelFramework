

class SignInPage:

    @staticmethod
    def sign_in_page_header():
        return "//h1[text()='Sign In']"

    @staticmethod
    def sign_in_page_title():
        return "//h1[text()='Sign In']/../p"

    @staticmethod
    def submit_log_in():
        return "//button[text()='Log In']"

    @staticmethod
    def email_error():
        return "//span[text()='Please provide your email address.']"



