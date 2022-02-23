import unittest
from execute import *


class TestGeneric(unittest.TestCase):
    """
    Will test the execution function
    """

    def test_when_weight_none_bmi_none(self):
        actual_output = compute_bmi(None, 171)
        self.assertEqual(actual_output, None)

    def test_when_height_none_bmi_none(self):
        actual_output = compute_bmi(96, None)
        self.assertEqual(actual_output, None)

    def test_is_bmi_correct(self):
        expected_output = 32.8
        actual_output = compute_bmi(96, 171)
        self.assertEqual(actual_output, expected_output)

    def test_when_bmi_none_category_none(self):
        actual_output = generate_category(None)
        self.assertEqual(actual_output, None)

    def test_is_category_correct(self):
        expected_output = 'Moderately obese'
        actual_output = generate_category(32.8)
        self.assertEqual(actual_output, expected_output)

    def test_when_category_none_risk_none(self):
        actual_output = generate_risk(None)
        self.assertEqual(actual_output, None)

    def test_is_risk_correct(self):
        expected_output = 'Medium risk'
        actual_output = generate_risk('Moderately obese')
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
