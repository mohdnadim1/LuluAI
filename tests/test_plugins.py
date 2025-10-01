import unittest
from luluai.plugins.builtins import CalculatorPlugin

class TestCalculatorPlugin(unittest.TestCase):
    """
    Tests for the CalculatorPlugin.
    """

    def setUp(self):
        """
        Set up a new CalculatorPlugin instance for each test.
        """
        self.plugin = CalculatorPlugin()

    def test_addition(self):
        """
        Test that the plugin can perform addition.
        """
        result = self.plugin.process("2 + 2")
        self.assertEqual(result, "The result is 4.")

    def test_subtraction(self):
        """
        Test that the plugin can perform subtraction.
        """
        result = self.plugin.process("10 - 5")
        self.assertEqual(result, "The result is 5.")

    def test_multiplication(self):
        """
        Test that the plugin can perform multiplication.
        """
        result = self.plugin.process("3 * 7")
        self.assertEqual(result, "The result is 21.")

    def test_division(self):
        """
        Test that the plugin can perform division.
        """
        result = self.plugin.process("10 / 2")
        self.assertEqual(result, "The result is 5.0.")

    def test_invalid_expression(self):
        """
        Test that the plugin handles invalid expressions gracefully.
        """
        result = self.plugin.process("2 +")
        self.assertIn("Error", result)

    def test_unsafe_expression(self):
        """
        Test that the plugin handles unsafe expressions.
        """
        result = self.plugin.process("__import__('os').system('echo unsafe')")
        self.assertIn("Error", result)

if __name__ == "__main__":
    unittest.main()