

import unittest
from pathlib import Path
from Reusable.reusable_methods import ReusableTest
from Reusable import Driver
from TestScenarioImplementation.HomeTestDef import HomeTestDef


class HomeTest(unittest.TestCase):


    def setUp(self):

        Driver.Initialize()

    def test_scenarios_execution(self):

        pro_path = Path(__file__).parent
        x = str(pro_path).split("TestScenarios")[0] + str("TestReport/")
        with open(x + 'mypage.html', 'w') as html_file:

            # Create initial test report
            ReusableTest.initial_html(html_file)

            # Starting execution
            HomeTestDef.go_to_url(ReusableTest.read_xml("applicationurl"))  # Launch The Application
            HomeTestDef.header_options_validation(self, html_file)  # Do Header section validation
            HomeTestDef.footer_options_validation(self, html_file)  # Do Footer section validation

            # Final report
            ReusableTest.final_html(html_file)

    def tearDown(self):
        Driver.close_driver()


if __name__ == '__main__':
    unittest.main()
