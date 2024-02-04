from OLlexer import TokenType
class NodeType():
    ProgramType = "ProgramType"
    NumLit = "NumLit"
    Ident = "Ident"
    BinExp = "BinExp"

class Statement():
    kind: NodeType
    value: any
class Program(Statement):
    kind: NodeType.ProgramType
    value: list
    
class BinaryExpression():
    kind: "BinExp"
    left: Statement
    right: Statement
    op: str

    def __str__(self) -> str:
        return str(self.left)+str(self.op)+str(self.right) ## Returns string of the two concanatated items

