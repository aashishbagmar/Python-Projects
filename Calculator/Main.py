# def sum(f_number, s_number):
#     total = f_number + s_number
#     print(f"{f_number} + {s_number} = {total}")
    
# def multiply(f_number, s_number):
#     total = f_number * s_number
#     print(f"{f_number} * {s_number} = {total}")

# def divide(f_number, s_number):
#     total = f_number / s_number
#     print(f"{f_number} / {s_number} = {total}")

# def substraction(f_number, s_number):
#     total = f_number - s_number
#     print(f"{f_number} - {s_number} = {total}")

# f_number = float(input("What's the first number?: "))
# operation = input(" + \n - \n * \n / \n Pick an operation: ")
# s_number = float(input("What's the next number?: "))

# if operation == "+":
#     sum(f_number, s_number)
# elif operation == "-":
#     substraction(f_number, s_number)
# elif operation == "/":
#     divide(f_number, s_number)
# elif operation == "*":
#     multiply(f_number, s_number)

# condition = input("Type 'y' to continue calculating with {total}, or type 'n' to start a new calculation: ")

def add(n1, n2):
    return n1+n2

def substract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

def clear():
    print("\n" * 50)


operation = {
    "+" : add,
    "-" : substract,
    "/" : divide,
    "*" : multiply,
}
def calculator():
    num1 = float(input("What is the first number : "))
    for symbol in operation:
        print(symbol)
    should_continue = True

    while should_continue :
        operation_symbol = input("Pick an operation : ")
        num2 = float(input("What is the second number : "))
        calculation_function = operation[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y' :
            num1 = answer
        else:
            should_continue = False
            clear() 
            calculator()

calculator()



