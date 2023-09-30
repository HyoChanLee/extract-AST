from pycparser import c_parser, c_ast

c_code = """
(C코드 입력)
"""

# AST 생성
parser = c_parser.CParser()
ast = parser.parse(c_code)

# 함수의 개수, 함수들의 리턴타입, 함수의 이름, 파라미터의 타입과 변수명, if 조건문의 개수 추출
functions = []

class FuncDefVisitor(c_ast.NodeVisitor):
    def visit_FuncDef(self, node):
        if isinstance(node.decl.type, c_ast.FuncDecl):
            return_type = "반환 타입: " + " ".join(node.decl.type.type.type.names)
            params = [(param.type.type.names, param.name) for param in node.decl.type.args.params]
            params_str = "파라미터: " + ", ".join(f"({param_type} {param_name})" for param_type, param_name in params)
            func_info = {
                "name": "함수 이름: " + node.decl.name,
                "return_type": return_type,
                "params": params_str,
                "if_count": 0
            }
            functions.append(func_info)
        self.generic_visit(node)

    def visit_If(self, node):
        functions[-1]["if_count"] += 1
        self.generic_visit(node)

func_def_visitor = FuncDefVisitor()
func_def_visitor.visit(ast)

# 결과 출력
for func in functions:
    print(func["name"])
    print(func["return_type"])
    print(func["params"])
    print("if문 개수:", func["if_count"])
    print("=" * 30)
