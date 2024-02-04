
from parser import Parser
from oliAst import BinaryExpression, Statement

parser = Parser()

print("REPL v0.1")

while True:
    prompt = input("> ")
    val = Parser.parseMULTExp(prompt)
    print(val)
