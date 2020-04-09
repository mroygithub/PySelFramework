

import unittest
from Reusable.reusable_methods import ReusableTest
from Reusable import Driver
from TestScenarioImplementation.HomeTestDef import HomeTestDef


class HomeTest(unittest.TestCase):

    def setUp(self):

        Driver.Initialize()

    def test_scenarios_execution(self):

        HomeTestDef.GoToURL(ReusableTest.read_xml("applicationurl"))  # Launch The Application
        HomeTestDef.header_options_validation(self)  # Do Header section validation
        HomeTestDef.footer_options_validation(self)  # Do Footer section validation

    def tearDown(self):
        Driver.close_driver()


if __name__ == '__main__':
    unittest.main()
