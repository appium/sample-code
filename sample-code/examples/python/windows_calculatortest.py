"""
//******************************************************************************
//
// Copyright (c) 2016 Microsoft Corporation. All rights reserved.
//
// This code is licensed under the MIT License (MIT).
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
// THE SOFTWARE.
//
//******************************************************************************
"""

import unittest
from appium import webdriver

class SimpleCalculatorTests(unittest.TestCase):

    def setUp(self):
        #set up appium
        desired_caps = {}  
        desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
        desired_caps["platformName"] = "Windows"
        desired_caps["deviceName"] = "WindowsPC"
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities= desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_initialize(self):
        #Make sure we're in standard mode
        self.driver.find_element_by_xpath("//Button[starts-with(@Name, \"Menu\")]").click();
        self.driver.find_element_by_xpath("//ListItem[@Name=\"Standard Calculator\"]").click();

        self.driver.find_element_by_name("Clear").click()
        self.driver.find_element_by_name("Seven").click()

        result = self.driver.find_element_by_accessibility_id("CalculatorResults")
        self.assertEqual(str(result.text),"Display is  7 ")

    def test_addition(self):
        self.driver.find_element_by_name("One").click()
        self.driver.find_element_by_name("Plus").click()
        self.driver.find_element_by_name("Seven").click()
        self.driver.find_element_by_name("Equals").click()

        result = self.driver.find_element_by_accessibility_id("CalculatorResults")
        self.assertEqual(str(result.text), "Display is  8 ")

    def test_combination(self):
        self.driver.find_element_by_name("Seven").click()
        self.driver.find_element_by_name("Multiply by").click()
        self.driver.find_element_by_name("Nine").click()
        self.driver.find_element_by_name("Plus").click()
        self.driver.find_element_by_name("One").click()
        self.driver.find_element_by_name("Equals").click()
        self.driver.find_element_by_name("Divide by").click()
        self.driver.find_element_by_name("Eight").click()
        self.driver.find_element_by_name("Equals").click()

        result = self.driver.find_element_by_accessibility_id("CalculatorResults")
        self.assertEqual(str(result.text), "Display is  8 ")

    def test_division(self):
        self.driver.find_element_by_name("Eight").click()
        self.driver.find_element_by_name("Eight").click()
        self.driver.find_element_by_name("Divide by").click()
        self.driver.find_element_by_name("One").click()
        self.driver.find_element_by_name("One").click()
        self.driver.find_element_by_name("Equals").click()
        
        result = self.driver.find_element_by_accessibility_id("CalculatorResults")
        self.assertEqual(str(result.text), "Display is  8 ")

    def test_multiplication(self):
        self.driver.find_element_by_name("Nine").click()
        self.driver.find_element_by_name("Multiply by").click()
        self.driver.find_element_by_name("Nine").click()
        self.driver.find_element_by_name("Equals").click()

        result = self.driver.find_element_by_accessibility_id("CalculatorResults")
        self.assertEqual(str(result.text), "Display is  81 ")

    def test_subtraction(self):
        self.driver.find_element_by_name("Nine").click()
        self.driver.find_element_by_name("Minus").click()
        self.driver.find_element_by_name("One").click()
        self.driver.find_element_by_name("Equals").click()

        result = self.driver.find_element_by_accessibility_id("CalculatorResults")
        self.assertEqual(str(result.text), "Display is  8 ")



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleCalculatorTests)
    unittest.TextTestRunner(verbosity=2).run(suite)