from art_calc import logo



# Add function
def add(n1, n2):
    return n1 + n2

# Subtract function
def subtract(n1, n2):
    return n1 - n2

# Multiply function
def multiply(n1, n2):
    return n1 * n2

# Divide function
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide
    }

num1 = int(input("What is your first number?: "))
print("which operation would you like to do?", end = " ")
print(*operations, end = " ")
operation_symbol = input(": ")
num2 = int(input("What is your second number: "))

function = operations[operation_symbol]
answer = function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")