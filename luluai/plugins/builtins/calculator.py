# luluai/plugins/builtins/calculator.py

class CalculatorPlugin:
    """
    A simple calculator plugin that evaluates a string expression.
    """

    def process(self, input_text):
        """
        Evaluates the input string as a Python expression.

        Warning: This uses eval() and is not safe for untrusted input.
        """
        try:
            # For safety, we can restrict the environment for eval
            # This is still not perfectly safe, but better than a wide-open eval
            allowed_globals = {"__builtins__": {}}
            result = eval(input_text, allowed_globals)
            return f"The result is {result}."
        except Exception as e:
            return f"Error: {e}"