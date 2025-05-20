# This import is fo
import re

# List of keywords and symbols
KEYWORDS = {'if': 'IF', 'while': 'WHILE', 'print': 'PRINT'}
SYMBOLS = {
    '=': 'ASSIGN',
    '+': 'PLUS',
    '-': 'MINUS',
    '*': 'MULT',
    '/': 'DIV',
    '==': 'EQ',
    '!=': 'NEQ',
    '>': 'GT',
    '<': 'LT',
    '>=': 'GTE',
    '<=': 'LTE',
    ':': 'COLON',
    '(': 'LPAREN',
    ')': 'RPAREN'
}

def lexer(code):
    tokens = []
    lines = code.split('\n')
    indent_stack = [0]

    
    for line_num, line in enumerate(lines, start=1):

        # Skip empty lines
        if not line.strip():
            continue

        # Ignore everything after a comment
        comment_index = line.find('#')
        if comment_index != -1:
            line = line[:comment_index]

        # Handle indentation
        # This keeps track of the current indentation level
        indent = len(line) - len(line.lstrip(' '))
        if indent > indent_stack[-1]:
            tokens.append(('INDENT', '', line_num))
            indent_stack.append(indent)
        while indent < indent_stack[-1]:
            tokens.append(('DEDENT', '', line_num))
            indent_stack.pop()


        i = 0
        while i < len(line):
            c = line[i]

            # Ignore whitespace between tokens
            # Skip to the next line
            if c.isspace():
                i += 1
                continue

            # Keywords, identifiers
            if c.isalpha():
                start = i
                while i < len(line) and (line[i].isalnum() or line[i] == '_'):
                    i += 1
                word = line[start:i]
                token_type = KEYWORDS.get(word, 'ID')
                tokens.append((token_type, word, line_num))
                continue

            # Numbers
            if c.isdigit():
                start = i
                while i < len(line) and line[i].isdigit():
                    i += 1
                tokens.append(('NUMBER', line[start:i], line_num))
                continue

            # 2-character operators (==, !=, >=, <=)
            if i + 1 < len(line) and line[i:i+2] in SYMBOLS:
                tokens.append((SYMBOLS[line[i:i+2]], line[i:i+2], line_num))
                i += 2
                continue

            # 1-character operators
            if c in SYMBOLS:
                tokens.append((SYMBOLS[c], c, line_num))
                i += 1
                continue

            # Unrecognized character
            tokens.append(('ERROR', c, line_num))
            i += 1
    
    return tokens

def main():
    filename = "tester.py"

    with open(filename, "r") as f:
        code = f.read()

    tokens = lexer(code)

    for token in tokens:
        print(token)

if __name__ == "__main__":
    main()