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
print(*operations, "which operation would you like to do?", end = " ")
operation_symbol = input(": ")
num2 = int(input("What is your second number: "))

function = operations[operation_symbol]
answer = function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")

# While loop to allow user to continue calculating with the answer
while True:
    
    end = input(f"Type 'y' to continue calculating with {answer} or type 'n' to exit: ").lower()
    if end == "n":
        break

    print(*operations, "which operation would you like to do?", end = " ")
    operation_symbol = input(": ")
    num3 = int(input("What is your next number: "))

    function = operations[operation_symbol]
    answer = function(answer, num3)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    


