class ErrorMessages:
    invalid_input ="ERROR: Invalid input"

def get_number(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print(ErrorMessages.invalid_input)

num1 = get_number("Enter a number: ")
num2 = get_number("Enter another number: ")
result = num1 + num2
print("The sum is", result)
