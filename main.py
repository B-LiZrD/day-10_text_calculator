import art
from replit import clear

# Calculator

# Add
def add(n1, n2):
  return n1 + n2


# Subtract
def subtract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  logo = art.logo
  print(logo)

  num1 = float(input("What is your first number? "))
  for symbol in operations:
    print(symbol)
  another_one = True

  while another_one:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What is your next number? "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    decision = input(f"Type 'y' to continue calculating with {answer}, 'n' for new calculation\nor 'e' to exit: ").lower()
    if decision == 'y':
      num1 = answer
    elif decision == 'n':
      another_one = False
      clear()
      calculator()
    else:
      print("Good-bye..")
      break

calculator()