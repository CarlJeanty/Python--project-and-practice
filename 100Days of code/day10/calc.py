#Calculator

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2


operations ={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    num1 = float(input("Enter the first number"))


    for  symbol in operations:
        print(symbol)
    should_countinue =True
    while should_countinue:
        operation_symbol = input("Pick an operator from the line above: ")
        num2 = float(input("Enter the second number"))
        #operations_calculator = operations[operation_symbol]
        # answer =operations[operation_symbol](num1, num2)
        answer = operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        previous = answer
        keep_going = input(f"Type 'y' to countinue calculation with {answer}. enter 'n' for a new start any oother letter to exit").lower()
        if keep_going =='y':
            num1 = answer
        elif keep_going=='n':
            calculator()
        else:
            should_countinue=False
calculator() # recursion infinite call of