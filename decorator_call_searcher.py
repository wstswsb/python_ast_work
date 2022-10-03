import ast
from decorator_call import DecoratorCall


class DecoratorCallsSearcher(ast.NodeVisitor):
    def __init__(self, decorator_name):
        self.__decorator_calls = []
        self.decorator_name = decorator_name

    def search(self, code):
        abstract_syntax_tree = ast.parse(code)
        self.visit(abstract_syntax_tree)
        result = self.__decorator_calls[:]
        self.__decorator_calls = []
        return result

    def visit_FunctionDef(self, node):
        for decorator in node.decorator_list:
            if isinstance(decorator, ast.Attribute):
                decorator_call = DecoratorCall.from_ast_attribute(decorator)
                self.__decorator_calls.append(decorator_call)
            if isinstance(decorator, ast.Call):
                decorator_call = DecoratorCall.from_ast_call(decorator)
                self.__decorator_calls.append(decorator_call)
