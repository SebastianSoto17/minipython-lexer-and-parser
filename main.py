from lexer import lexer
from parser import Parser


def main():
    filename = "tester.py"

    with open(filename, "r") as f:
        code = f.read()

    tokens = lexer(code)
    parser = Parser(tokens)
    ast = parser.parse()

    for node in ast:
        print(node)

if __name__ == "__main__":
    main()