fileERR = "LEXER ERR:"
class TokenType():
    Number = "Number"
    Identifer = "Identifier"
    Equals = "Equals"
    OpenParen = "OpenParen"
    CloseParen = "CloseParen"
    BinOperator = "BinOperator"
    Null = "Null" #IN PYTHON IS "None"
    Let = "Let"
    Def = "def"
    EOF = "EOF"

KEYWORDS = {"let": TokenType.Let, "def":TokenType.Def}
def shift(arr:list) -> list:
    curr = arr[0]
    arr = arr.pop(0)
    return curr

class Token():
    value : str
    type : TokenType

def token ( value: any, type:TokenType) -> Token:
    if (value != None):
        return {value, type}
    else:
        raise Exception(fileERR, "Trying to assign null value to Token")
    
def isalpha(src:str) -> bool: # sees if the character is alphabetic
    return src.upper() != src.lower()
def isint(src:str) -> bool: ## sees if the character is an int or not
    bounds = [ord("0") , ord("9")]
    num = ord(src)
    return num>= bounds[0] and num<= bounds[1]
def isskippable(src:str): ## sees if the character is whitespace
    return src == " " or src == "\n" or src == "\t"

def tokenize(source:str) -> list :
    tokens = list()
    src = list(source)
    while len(src) != 0:
        match src[0]:
            case "(":
                tokens.append(token(shift(src), TokenType.OpenParen))
            case ")":
                tokens.append(token(shift(src), TokenType.CloseParen))
            case "+" | "-" | "*" | "/" | "%":
                tokens.append(token(shift(src), TokenType.BinOperator))
            case "=":
                tokens.append(token(shift(src), TokenType.Equals))
            case _:
                ##MULTICHAR TOKENS
                if (isint(src[0])):
                    num = ""
                    while (len(src) > 0 and isint(src[0])):
                        num += shift(src)
                    tokens.append(token(num, TokenType.Number))
                elif (isalpha(src[0])):
                    ident = ""
                    while (len(src) > 0 and isalpha(src[0])):
                        ident += shift(src)
                    if (ident not in KEYWORDS): ## checks to see if the word already exists as a keyword
                        tokens.append(token(ident, TokenType.Identifer))
                    else:

                        tokens.append(token(ident, KEYWORDS[ident]))
                elif isskippable(src[0]):
                    shift(src)
                else:
                    print(fileERR,"Unrecognized character", src[0], "found in source during tokenization")
                    exit()
    tokens.append(token("EndOfFile", TokenType.EOF))            
    return tokens



