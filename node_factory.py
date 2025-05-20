from ast_nodes import *

class NodeFactory:
    @staticmethod
    def create(node_type, *args):
        if node_type == 'number':
            return NumberNode(*args)
        elif node_type == 'string':
            return StringNode(*args)
        elif node_type == 'identifier':
            return IdentifierNode(*args)
        elif node_type == 'binop':
            return BinOpNode(*args)
        elif node_type == 'assign':
            return AssignNode(*args)
        elif node_type == 'print':
            return PrintNode(*args)
        elif node_type == 'if':
            return IfNode(*args)
        else:
            raise ValueError(f"Unknown node type: {node_type}")
