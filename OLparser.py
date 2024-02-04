from OLast import NodeType, Statement, BinaryExpression
from OLlexer import TokenType, tokenize, token
from OLast import Program
fileERR = "PARSER ERR:"
class Parser():
    kind : NodeType.ProgramType
    prog = []
    def notEof(self) -> bool:
        return self.prog[0].type != TokenType.EOF
    def produceAST(self, src: str) -> Program: 
        if (type(src) != str):
            print(fileERR, "Trying to parse empty string or other object")
            exit()
        else:
            self.prog = tokenize(src)
            program = Program(kind: NodeType.program)

    def eat(self):
        prev = self.prog.pop()
        return prev
    def parseMULTExp(self, exp: BinaryExpression) -> Statement:
        if (exp.op == "*" or exp.op == "/" or exp.op == "%"):
            operator = self.eat()
        
    def ParseADDExp(exp:BinaryExpression):
        return self.parseMULTExp(exp)
    def parseExp(exp:BinaryExpression):
        return self.ParseADDExp(exp)
