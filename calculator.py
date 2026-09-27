import math


class Calculator:
    def _init_(self):
        self.history = []
        self.load_history()

    
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

    def power(self, a, b): return a ** b

    def modulo(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot use modulo with zero.")
        return a % b

    def square_root(self, a):
        if a < 0:
            raise ValueError("Cannot calculate the square root of a negative number.")
        return math.sqrt(a)

   
    def add_to_history(self, calculation):
        self.history.append(calculation)
        self.save_history()  # Save instantly when updated

    def show_history(self):
        if not self.history:
            print("\nNo calculations in history.")
            return
        print("\n--- Calculation History ---")
        for index, calculation in enumerate(self.history, start=1):
            print(f"{index}. {calculation}")

    def clear_history(self):
        self.history.clear()
        self.save_history()
        print("\nHistory cleared successfully.")

    
    def save_history(self):
        try:
            with open("history.txt", "w", encoding="utf-8") as file:
                for calculation in self.history:
                    file.write(calculation + "\n")
        except OSError as error:
            print(f"Could not save history: {error}")

    def load_history(self):
        try:
            with open("history.txt", "r", encoding="utf-8") as file:
                self.history = [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            self.history = []
        except OSError as error:
            print(f"Could not load history: {error}")
            self.history = []


def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def perform_calculation(calculator, choice):
    try:
        if choice == "7":
            number = get_number("Enter a number: ")
            result = calculator.square_root(number)
            calculation = f"√{number} = {result}"
        else:
            number1 = get_number("Enter the first number: ")
            number2 = get_number("Enter the second number: ")

            operations = {
                "1": (calculator.add, "+"),
                "2": (calculator.subtract, "-"),
                "3": (calculator.multiply, "×"),
                "4": (calculator.divide, "÷"),
                "5": (calculator.power, "^"),
                "6": (calculator.modulo, "%")
            }

            func, symbol = operations[choice]
            result = func(number1, number2)
            calculation = f"{number1} {symbol} {number2} = {result}"

        print(f"Result: {result}")
        calculator.add_to_history(calculation)

    except (ZeroDivisionError, ValueError) as error:
        print(f"Error: {error}")


def main():
    calculator = Calculator()

    while True:
        print("\n" + "=" * 30)
        print("        PYTHON CALCULATOR")
        print("=" * 30)
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Power")
        print("6. Modulo\n7. Square Root\n8. Show History\n9. Clear History\n10. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "10":
            print("Goodbye!")
            break
        elif choice == "8":
            calculator.show_history()
        elif choice == "9":
            calculator.clear_history()
        elif choice in [str(i) for i in range(1, 8)]:
            perform_calculation(calculator, choice)
        else:
            print("Invalid option. Please choose a number from 1 to 10.")


if __name__ == "_main_":
    main()