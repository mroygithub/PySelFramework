

import unittest
from pathlib import Path
from Reusable.reusable_methods import ReusableTest
from Reusable import Driver
from TestScenarioImplementation.SignInTestDef import SignInTestDef


class SignInTestClass(unittest.TestCase):

    def setUp(self):

        Driver.Initialize()

    def test_scenarios_execution(self):

        pro_path = Path(__file__).parent
        x = str(pro_path).split("TestScenarios")[0] + str("TestReport/")
        with open(x + 'SignInTestScenario.html', 'w') as html_file:

            # Create initial test report
            ReusableTest.initial_html(html_file, "Sign In Test Scenario")

            # Starting execution
            SignInTestDef.go_to_url(ReusableTest.read_xml("applicationurl"))  # Launch The Application
            SignInTestDef.sign_in_header(self, html_file)  # Do Header section validation
            SignInTestDef.sign_in_body(self, html_file)  # Do negative sign in  section validation

            # Final report
            ReusableTest.final_html(html_file)

    def tearDown(self):
        Driver.close_driver()


if __name__ == '__main__':
    unittest.main()
