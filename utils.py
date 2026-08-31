# utils.py


def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value

        except ValueError:
            print("Please enter a valid number.")


def get_unit(prompt):
    while True:
        unit = input(prompt).strip().lower()

        if unit:
            return unit

        print("Unit cannot be empty.")


def show_result(value, from_unit, result, to_unit):
    print()
    print(f"{value:g} {from_unit} = {result:.2f} {to_unit}")
    print()


def show_menu():
    print("\n===== Converter =====")
    print("1. Currency Converter")
    print("2. Length Converter")
    print("3. Weight Converter")
    print("4. Temperature Converter")
    print("5. Exit")