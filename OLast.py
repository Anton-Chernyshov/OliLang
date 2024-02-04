class NodeType():
    ProgramType = "ProgramType"
    NumLit = "NumLit"
    Ident = "Ident"
    BinExp = "BinExp"

class Statement():
    kind: NodeType
    value: any
class BinaryExpression():
    kind: "BinExp"
    left: Statement
    right: Statement
    op: str

    def __str__(self) -> str:
        return str(self.left)+str(self.op)+str(self.right) ## Returns string of the two concanatated items




x = BinaryExpression()
y = BinaryExpression()
y.left = 2
y.right = 3
y.op = "+"
x.left = y
x.right = 10
x.op = "+"
print(x)