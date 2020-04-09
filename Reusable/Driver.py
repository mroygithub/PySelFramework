
# Created on Oct 24, 2017
# @author: mithun_roy

from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
import selenium.webdriver.support.ui as ui
from Reusable.reusable_methods import ReusableTest

Instance = None


def Initialize():

    global Instance
    Instance = webdriver.Chrome(ReusableTest.read_xml("chrome_path"))
    # Instance = webdriver.Ie("C:\IEDriverServer")
    Instance.implicitly_wait(10)
    return Instance

# To Do Login Scenarios


def login(self, uid, pw):
    try:
        # ClickandImplicitWait(CreateAnAccountPage.login_button())
        # TypeText(CreateAnAccountPage.login_email(), uid)
        # TypeText(CreateAnAccountPage.login_password(), pw)
        # ClickandExplicitWait(CreateAnAccountPage.login_submit_button(), 5)
        Instance.implicitly_wait(30)
        return True
    except:
        return False


# CHECK FOR ELEMENT

def is_web_element_displayed(element):
    try:
        timeout = 3
        wait = ui.WebDriverWait(Instance, timeout)
        wait.until(
            lambda driver: driver.find_element_by_xpath(element).is_displayed())
        print ("Element  available")
        return True
    except:
        print("Element not available")
    return False


# CLICK AND IMPLICIT WAIT


def click_and_implicit_wait(element):
    try:
        if Instance.find_element_by_xpath(element).is_displayed():
            Instance.find_element_by_xpath(element).click()
            Instance.implicitly_wait(30)
            return True
        else:
            return False
    except:
        return False

# TO Retrieve Expected Web Element


def expected_web_element(element, expected_number):
    try:
        if len(Instance.find_elements_by_xpath(element)) == expected_number:
            return True
        else:
            return False
    except:
        return False

# TO Retrieve Expected Web Element


def web_element_count(element):
        try:
            if len(Instance.find_elements_by_xpath(element)) > 0:
                return len(Instance.find_elements_by_xpath(element))
            else:
                return 0
        except:
            return 0

# CLICK AND EXPLICIT WAIT


def click_and_explicit_wait(element, time):
    try:
        if Instance.find_element_by_xpath(element).is_displayed():
            Instance.find_element_by_xpath(element).click()
            sleep(time)
            return True
        else:
            return False
    except:
        return False

# PRESS Enter With Focus


def focus_and_press_enter(element, time):
    try:
        if Instance.find_element_by_xpath(element).is_displayed():
            Instance.find_element_by_xpath(element).send_keys("\n")
            sleep(time)
            return True
        else:
            return False
    except:
        return False

# TYPE TEXT BOX


def type_text(element, text):
    try:
        if Instance.find_element_by_xpath(element).is_displayed():
            Instance.find_element_by_xpath(element).clear()
            Instance.find_element_by_xpath(element).send_keys(text)
            return True
        else:
            return False
    except:
        return False

# SELECT A DROP DOWN


def select_drop_down(element, option):
    try:
        if Instance.find_element_by_xpath(element).is_displayed():
            select = Select(Instance.find_element_by_xpath(element))
            select.select_by_visible_text(option)
            return True
        else:
            return False
    except:
        return False

# RETURN ELEMENT TEXT


def get_element_text(element):
    try:
        if Instance.find_element_by_xpath(element).is_displayed():
            return Instance.find_element_by_xpath(element).text
    except:
        return "NO TEXT"

# Implicit Wait


def implicit_wait(t):
    Instance.implicitly_wait(t)

# Implicit Wait


def explicit_wait(t):
    sleep(t)


# Navigate Back


def go_back(t):
    Instance.back()
    sleep(t)


# TO CLOSE THE BROWSER


def close_driver():
    global Instance
    Instance.quit()