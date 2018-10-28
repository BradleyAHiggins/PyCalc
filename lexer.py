class Token:
    opDict = {'+' : "ADD", '-' : "SUB", '/' : "DIV", '*' : "MULT", '^' : "EXP"}

    def __init__(self):
        return self

    def isInt(express):
        """isInt accepts a string, express, and tests whether express is an integer, returning True or False accordingly"""
        intString = "0123456789"
        for lex in express:
            if lex in intString:
                continue
            else:
                return False
        return True

    def isWhite(lexeme): 
        """isWhite accepts a char, lexeme and tests whether that lexeme is a white space character, returning True of False"""
        white = ' '
        if lexeme == white:
            return True
        else:
            return False

    def isOperator(lexeme):
        "isOperator accepts a char, lexeme, and tests whether or not it is a valid operator; returns True of False"""
        for keys in Token.opDict:
            if keys == lexeme:
                return True
            else:
                continue
        return False

    def isDecimal(lexeme):
        """isDecimal accepts a char, lexeme, and tests whether it is a decimal character; returns True of False"""
        if lexeme == '.':
            return True
        else:
            return False

    def isLeft(lexeme):
        """isLeft accepts a lexeme and tests whether it is a left parthesis, '('; returns True of False"""
        if lexeme == '(':
            return True
        else:
            return False

    def isRight(lexeme):
        """isLeft accepts a lexeme and tests whether it is a left parthesis, '('; returns True of False"""
        if lexeme == ')':
            return True
        else:
            return False
    
    def isFloat(substr):
        """isFloat accepts a string and tests whether that string represents a floating point number; returns True or False"""
        if not Token.isInt(substr[0]) or not Token.isInt(substr[len(substr) - 1]):
            return False
        if '.' in substr:
            return True
        else:
            return False
     
    def isDelim(lexeme):
        """isDelim accepts a lexeme and tests whether that lexeme is a delimiter or not; returns True of False"""
        if Token.isLeft(lexeme) or Token.isRight(lexeme) or Token.isWhite(lexeme) or Token.isOperator(lexeme):
            return True
        else:
            return False

   

class Operator(Token):
    """The Operator class is a Token that holds the value of an operator character and an ID value"""
    def __init__(self, op):
        # accepted operators: +-/*^
        self.value = op
        for keys in Token.opDict:
            if keys == op:
                self.ID = Token.opDict[keys]
                break
        if self.ID == "EXP":
            self.precedence = 4
        elif self.ID == "MUlT" or self.ID == "DIV":
            self.precedence = 3
        else:
            self.precedence = 2
    

class Integer(Token):
    """The Operator class is a Token that holds the value of an Integer lexeme and an ID value"""
    def __init__(self, val):
        self.value = int(val)
        self.ID = "INT"
    

class FloatP(Token):
#float := {0..9}[0..9]...[0..9].{0..9}[0..9]...
    #TODO: add __init__
    pass

class SpecialFunc(Token):
    pass

class WhiteSpace(Token):

    def __init__(self, lexeme):
        self.ID ="WHITE"
        self.value = lexeme
        
class Parenthesis(Token):
    def __init__(self, lexeme):
        self.ID = "PAREN"
        self.precedence = 0
        if Token.isRight(lexeme):
            self.value = "RIGHT"
        elif Token.isLeft(lexeme):
            self.value = "LEFT"

def stripWhite(tokens):
    """stripWhite accepts a tokenized string, represented as a list and named 'tokens' and strips the WHITE  tokens from the list, returning the white-less list"""
    for tok in tokens:
        if tok.ID == "WHITE":
            tokens.remove(tok)

def tokenizer(expression):
    """tokenizer accepts a string, named 'expression', and analyzes it for tokens, and returns a tokenized representation of 'expression' as a list.

    tokenizer makes a call to 'stripWhite' before returning the tokenized list. Each element of the returned list is one of the classes defined in the lexer.py module.
    """
    start, current, end = 0, 0 , len(expression) - 1
    tokenizedExpression = []
    while current <= end:
        if Token.isDelim(expression[current]):
            start = current + 1
            if Token.isWhite(expression[current]):
                tokenizedExpression.append(WhiteSpace(expression[current]))
            elif Token.isOperator(expression[current]):
                tokenizedExpression.append(Operator(expression[current]))
            elif Token.isLeft(expression[current]) or Token.isRight(expression[current]):
                tokenizedExpression.append(Parenthesis(expression[current]))
            #single char token
        else:
            #one or more char token
            
            next = current + 1
            if next >= end:
                next = end
            if Token.isDelim(expression[next]) or current == end :
                
                pos = current + 1
                #__________________________________________________________________________________________________________________________
                #DEBUG
                #print("start:",start,"\ncurrent:",current,"\nnext:",next,"\npos:", pos,"\nexpression[start: pos]:",expression[start: pos])
                #__________________________________________________________________________________________________________________________
                if Token.isInt(expression[start: pos]):
                    tokenizedExpression.append(Integer(expression[start: pos]))
                elif Token.isFloat(expression[start: pos]):
                    pass
                    #uncomment when FloatP.__init__() is defined
                    #tokenizedExpression.append(FloatP(expression[start: next]))
                else:
                    #raise exception
                    pass
                start = current
            else:
                pass
    
        current += 1
    stripWhite(tokenizedExpression) 	    
    return tokenizedExpression

if __name__ == "__main__":
    tokens = tokenizer(input(">"))
    for tok in tokens:
        print(tok.ID,"    ", tok.value)

