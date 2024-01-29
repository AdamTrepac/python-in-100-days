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

def exponent(n1, n2):
    if n1 <= 0:
        return 1
    answer = 1
    for i in range(int(n2)):
        answer *= n1
    return answer


def calculator():
    print(logo)
    
    num1 = float(input("What is your first number?: "))
    # While loop to allow user to continue calculating with the answer
    while True:

        print(*operations, "which operation would you like to do?", end = " ")
        operation_symbol = input(": ")
        num2 = float(input("What is your next number: "))

        function = operations[operation_symbol]
        answer = function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        num1 = answer

        end = input(f"Type 'y' to continue calculating with {answer}, type 'c' to clear, or 'q' to quit: ").lower()
        if end == "c":
            calculator()
        elif end == "q":
            return

operations = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide,
    "^": exponent
    }

calculator()
print("goodbye")
