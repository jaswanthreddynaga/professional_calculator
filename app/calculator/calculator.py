"""
Main application file with REPL, input validation, and history.
"""
import sys
from app.calculation.factory import CalculationFactory
from app.calculation.calculation import Calculation

class Calculator:
    """
    A professional-grade command-line calculator with a REPL interface.
    """
    def __init__(self):
        self.history = []
        self.factory = CalculationFactory()

    def _display_help(self):
        """Displays available commands and instructions."""
        print("\n--- Calculator Help ---")
        print("Enter a calculation in the format: <number> <operator> <number>")
        print("Supported operators: +, -, *, /")
        print("Special Commands:")
        print("  help      : Show this help message.")
        print("  history   : Show calculation history.")
        print("  exit      : Exit the calculator.")
        print("-----------------------\n")

    def _display_history(self):
        """Displays the calculation history."""
        if not self.history:
            print("History is empty.")
            return

        print("\n--- Calculation History ---")
        for i, calc in enumerate(self.history):
            # Using the __str__ method of the Calculation class
            print(f"{i+1}. {calc}")
        print("---------------------------\n")

    def _validate_and_parse_input(self, user_input):
        """
        Validates and parses the user input for a calculation.

        Uses LBYL (Look Before You Leap) to check input structure
        and EAFP (Easier to Ask Forgiveness than Permission) to handle
        number conversion errors.
        """
        parts = user_input.split()
        if len(parts) != 3:
            raise ValueError("Invalid format. Use: <number> <operator> <number>")

        operand_a_str, operator_symbol, operand_b_str = parts

        # LBYL: Check for valid operator before attempting calculation
        if operator_symbol not in CalculationFactory.OPERATIONS:
             raise ValueError(f"Invalid operator: {operator_symbol}")

        # EAFP: Attempt to convert strings to floats
        try:
            operand_a = float(operand_a_str)
            operand_b = float(operand_b_str)
        except ValueError:
            raise ValueError("Operands must be valid numbers.")

        return operand_a, operand_b, operator_symbol

    def repl(self):
        """The Read-Eval-Print Loop (REPL) for the calculator."""
        print("Welcome to the Modular CLI Calculator!")
        self._display_help()

        while True:
            try:
                user_input = input("Calc > ").strip().lower()

                if not user_input:
                    continue # pragma: no cover

                if user_input == 'exit':
                    print("Exiting calculator. Goodbye!")
                    break
                elif user_input == 'help':
                    self._display_help()
                    continue
                elif user_input == 'history':
                    self._display_history()
                    continue

                # 1. Read & Validate
                operand_a, operand_b, operator_symbol = self._validate_and_parse_input(user_input)

                # 2. Eval (Create Calculation)
                calculation = self.factory.create_calculation(operand_a, operand_b, operator_symbol)

                # 3. Perform and Print
                result = calculation.perform()
                print(f"Result: {result}")

                # 4. Management (History)
                self.history.append(calculation) # Store the successful calculation

            except ValueError as e:
                # Catch custom ValueErrors (from validation or Division by Zero)
                print(f"Error: {e}")
            except Exception as e: # pragma: no cover
                # General error handling for unexpected issues
                print(f"An unexpected error occurred: {e}")

if __name__ == "__main__": # pragma: no cover
    # Entry point for running the application directly
    # Note: In a real professional project, you'd typically use a setup.py
    # or pyproject.toml and a script/entry point for launching.
    app = Calculator()
    app.repl()