from OLast import NodeType, Statement, BinaryExpression


class Parser():
    kind : NodeType.ProgramType
    prog = []
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
