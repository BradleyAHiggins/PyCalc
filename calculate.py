
def toPostFixN(tokens):
    output = []
    operators = []
    valid_operators = {"ADD" : "LEFT", "SUB": "LEFT", "MULT": "LEFT", "DIV" : "LEFT", "EXP" : "RIGHT"}
    
    for tok in tokens:
        if tok.ID == "INT" or tok.ID == "FLOAT":
            output.append(tok)
        elif tok.ID == "PAREN":
            if tok.value == "LEFT":
                operators.append(tok)
            else:
                opcopy = operators.copy()
                opcopy.reverse()
                left_found = False
                for op in opcopy:
                    if op.value == "LEFT":
                        left_found == True
                        operators.pop()
                        break
                    else:
                        output.append(operators.pop())
                if not left_found:
                    #raise exception for mismathed parenthesis
                    pass
        elif tok.ID in valid_operators:
            opcopy = operators.copy()
            opcopy.reverse()
            precedence_count = 0
            if len(opcopy) == 0:
                operators.append(tok)
            else:
                for i in range(0,len(opcopy)):
                    if opcopy[i].ID == "LEFT":
                        break
                    else:
                         if opcopy[i].precedence > tok.precedence:
                             precedence_count += 1
                         elif opcopy[i].precedence == tok.precedence and valid_operators[opcopy[i].ID] == "LEFT":
                             precedence_count += 1
                         else:
                             break
                for j in range(1, precedence_count):
                    output.append(operators.pop())
                operators.append(tok)
        else:
            #raise exception for invalid token
            pass

    while len(operators) > 0:
        output.append(operators.pop())
    return output
def addition(firstNum, secondNum):
    return firstNum + secondNum
def subtraction(firstNum, secondNum):
    return firstNum - secondNum
def multiply(firstNum, secondNum):
    return firstNum * secondNum
def divide(dividend, divisor):
    return dividend / divisor
def exponent(number, expon):
    return number**expon
def calcExpression(tokens):
    calcStack = []
    valid_operators = ["ADD", "SUB", "MULT", "DIV", "EXP"]
    for tok in tokens:
        if tok.ID == "INT" or tok.ID == "FLOAT":
            calcStack.append(tok.value)
        elif tok.ID in valid_operators:
            if len(calcStack) >= 2:
                secondNum = calcStack.pop()
                firstNum = calcStack.pop()
                if tok.ID == "ADD":
                    calcStack.append(addition(firstNum, secondNum))
                elif tok.ID == "SUB":
                    calcStack.append(subtraction(firstNum, secondNum))
                elif tok.ID == "MULT":
                    calcStack.append(multiply(firstNum, secondNum))
                elif tok.ID == "DIV":
                    calcStack.append(divide(firstNum, secondNum))
                elif tok.ID == "EXP":
                    calcStack.append(exponent(firstNum, secondNum))
            else:
                #raise invalid expression error
                pass
        else:
            #raise parsing error
            pass
    if len(calcStack) != 1:
        pass
        #raise invalid expression error
    else:
        return calcStack.pop()

