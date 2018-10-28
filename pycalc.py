import lexer as lx
import calculate as calc
version_number = "0.1"

def printWelcomeMessage():
    global version_number
    print("Welcome to pycalc.py version ",version_number,".")
    print("For a list of supported operators and functions, enter 'h'.")
    print("To exit, type 'exit'.")
    print("Please input your expression: ")

def printHelpMessage():
    global version_number
    supported_operations = ["Addition", "Subtraction", "Multplication", "Division", "Exponents"]
    supported_operation_symbols = ['+','-','*','/','^']
    print("pycalc.py version", version_number, "supports the following operations:")
    for operation in supported_operations:
        print(operation)
    print("represented by these operation symbols:")
    for symbol in supported_operation_symbols:
        print(symbol)
    
if __name__ == "__main__":
    printWelcomeMessage()
    exit_status = False
    while not exit_status:
        user_input = str(input(">"))
        if user_input == "h":
            printHelpMessage()
        elif user_input == "exit":
            exit_status = True
        else:
            tokenized_list = lx.tokenizer(user_input)
            postFixList = calc.toPostFixN(tokenized_list)
            answer = calc.calcExpression(postFixList)
            print(answer)

    print("Goodbye!")
