from art import logo
from replit import clear


def add(first_number, next_number):
  """returns the addition of two numbers"""
  return first_number + next_number


def subtract(first_number, next_number):
  """returns the subtraction of two numbers"""
  return first_number - next_number


def multiply(first_number, next_number):
  """returns the multiplication of two numbers"""
  return first_number * next_number


def divide(first_number, next_number):
  """returns the division of two numbers"""
  return first_number / next_number


def calcu():
  finish_calc = True
  operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
  print(logo)
  first_number = float(input("What's the First number?: "))
  score = 0
  for operator in operations:
    print(operator)
  while finish_calc:
    operation_symbol = input("Pick an operation: ")
    next_number = float(input("what's the next number?: "))
    # gets the function being called using operation symbol user inputted
    calculation_func = operations[operation_symbol]
    score = calculation_func(first_number, next_number)
    print(f"{first_number} {operation_symbol} {next_number} = {score}")
    continue_calc = input(
        f"Type y to continue calculating with {score} or type n to "
        "start a new calculation: ")
    if continue_calc == "y":
      first_number = score
      clear()
    else:
      finish_calc = False
      clear()
      calcu()


calcu()
