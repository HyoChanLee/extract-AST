import json

json_data = """
{
    "_nodetype": "FileAST",
    "coord": null,
    "ext": [
        {
            "_nodetype": "FuncDef",
            "body": {
                "_nodetype": "Compound",
                "block_items": [
                    {
                        "_nodetype": "If",
                        "cond": {
                            "_nodetype": "BinaryOp",
                            "coord": "hello.c:2:9",
                            "left": {
                                "_nodetype": "ID",
                                "coord": "hello.c:2:9",
                                "name": "a"
                            },
                            "op": ">",
                            "right": {
                                "_nodetype": "ID",
                                "coord": "hello.c:2:13",
                                "name": "b"
                            }
                        },
                        "coord": "hello.c:2:5",
                        "iffalse": {
                            "_nodetype": "Compound",
                            "block_items": [
                                {
                                    "_nodetype": "Return",
                                    "coord": "hello.c:5:9",
                                    "expr": {
                                        "_nodetype": "BinaryOp",
                                        "coord": "hello.c:5:16",
                                        "left": {
                                            "_nodetype": "ID",
                                            "coord": "hello.c:5:16",
                                            "name": "a"
                                        },
                                        "op": "-",
                                        "right": {
                                            "_nodetype": "ID",
                                            "coord": "hello.c:5:20",
                                            "name": "b"
                                        }
                                    }
                                }
                            ],
                            "coord": "hello.c:4:1"
                        },
                        "iftrue": {
                            "_nodetype": "Compound",
                            "block_items": [
                                {
                                    "_nodetype": "Return",
                                    "coord": "hello.c:3:9",
                                    "expr": {
                                        "_nodetype": "BinaryOp",
                                        "coord": "hello.c:3:16",
                                        "left": {
                                            "_nodetype": "ID",
                                            "coord": "hello.c:3:16",
                                            "name": "a"
                                        },
                                        "op": "+",
                                        "right": {
                                            "_nodetype": "ID",
                                            "coord": "hello.c:3:20",
                                            "name": "b"
                                        }
                                    }
                                }
                            ],
                            "coord": "hello.c:2:1"
                        }
                    }
                ],
                "coord": "hello.c:1:1"
            },
            "coord": "hello.c:1:5",
            "decl": {
                "_nodetype": "Decl",
                "align": [],
                "bitsize": null,
                "coord": "hello.c:1:5",
                "funcspec": [],
                "init": null,
                "name": "add",
                "quals": [],
                "storage": [],
                "type": {
                    "_nodetype": "FuncDecl",
                    "args": {
                        "_nodetype": "ParamList",
                        "coord": "hello.c:1:13",
                        "params": [
                            {
                                "_nodetype": "Decl",
                                "align": [],
                                "bitsize": null,
                                "coord": "hello.c:1:13",
                                "funcspec": [],
                                "init": null,
                                "name": "a",
                                "quals": [],
                                "storage": [],
                                "type": {
                                    "_nodetype": "TypeDecl",
                                    "align": null,
                                    "coord": "hello.c:1:13",
                                    "declname": "a",
                                    "quals": [],
                                    "type": {
                                        "_nodetype": "IdentifierType",
                                        "coord": "hello.c:1:9",
                                        "names": [
                                            "int"
                                        ]
                                    }
                                }
                            },
                            {
                                "_nodetype": "Decl",
                                "align": [],
                                "bitsize": null,
                                "coord": "hello.c:1:20",
                                "funcspec": [],
                                "init": null,
                                "name": "b",
                                "quals": [],
                                "storage": [],
                                "type": {
                                    "_nodetype": "TypeDecl",
                                    "align": null,
                                    "coord": "hello.c:1:20",
                                    "declname": "b",
                                    "quals": [],
                                    "type": {
                                        "_nodetype": "IdentifierType",
                                        "coord": "hello.c:1:16",
                                        "names": [
                                            "int"
                                        ]
                                    }
                                }
                            }
                        ]
                    },
                    "coord": "hello.c:1:5",
                    "type": {
                        "_nodetype": "TypeDecl",
                        "align": null,
                        "coord": "hello.c:1:5",
                        "declname": "add",
                        "quals": [],
                        "type": {
                            "_nodetype": "IdentifierType",
                            "coord": "hello.c:1:1",
                            "names": [
                                "int"
                            ]
                        }
                    }
                }
            },
            "param_decls": null
        },
        {
            "_nodetype": "FuncDef",
            "body": {
                "_nodetype": "Compound",
                "block_items": [
                    {
                        "_nodetype": "Return",
                        "coord": "hello.c:10:5",
                        "expr": {
                            "_nodetype": "BinaryOp",
                            "coord": "hello.c:10:12",
                            "left": {
                                "_nodetype": "ID",
                                "coord": "hello.c:10:12",
                                "name": "x"
                            },
                            "op": "*",
                            "right": {
                                "_nodetype": "ID",
                                "coord": "hello.c:10:16",
                                "name": "y"
                            }
                        }
                    }
                ],
                "coord": "hello.c:9:1"
            },
            "coord": "hello.c:9:7",
            "decl": {
                "_nodetype": "Decl",
                "align": [],
                "bitsize": null,
                "coord": "hello.c:9:7",
                "funcspec": [],
                "init": null,
                "name": "multiply",
                "quals": [],
                "storage": [],
                "type": {
                    "_nodetype": "FuncDecl",
                    "args": {
                        "_nodetype": "ParamList",
                        "coord": "hello.c:9:22",
                        "params": [
                            {
                                "_nodetype": "Decl",
                                "align": [],
                                "bitsize": null,
                                "coord": "hello.c:9:22",
                                "funcspec": [],
                                "init": null,
                                "name": "x",
                                "quals": [],
                                "storage": [],
                                "type": {
                                    "_nodetype": "TypeDecl",
                                    "align": null,
                                    "coord": "hello.c:9:22",
                                    "declname": "x",
                                    "quals": [],
                                    "type": {
                                        "_nodetype": "IdentifierType",
                                        "coord": "hello.c:9:16",
                                        "names": [
                                            "float"
                                        ]
                                    }
                                }
                            },
                            {
                                "_nodetype": "Decl",
                                "align": [],
                                "bitsize": null,
                                "coord": "hello.c:9:31",
                                "funcspec": [],
                                "init": null,
                                "name": "y",
                                "quals": [],
                                "storage": [],
                                "type": {
                                    "_nodetype": "TypeDecl",
                                    "align": null,
                                    "coord": "hello.c:9:31",
                                    "declname": "y",
                                    "quals": [],
                                    "type": {
                                        "_nodetype": "IdentifierType",
                                        "coord": "hello.c:9:25",
                                        "names": [
                                            "float"
                                        ]
                                    }
                                }
                            }
                        ]
                    },
                    "coord": "hello.c:9:7",
                    "type": {
                        "_nodetype": "TypeDecl",
                        "align": null,
                        "coord": "hello.c:9:7",
                        "declname": "multiply",
                        "quals": [],
                        "type": {
                            "_nodetype": "IdentifierType",
                            "coord": "hello.c:9:1",
                            "names": [
                                "float"
                            ]
                        }
                    }
                }
            },
            "param_decls": null
        }
    ]
}
"""

functions_data = json.loads(json_data)["ext"]

# 함수 정보 출력
for func in functions_data:
    print("함수 이름:", func["decl"]["name"])
    return_type = func["decl"]["type"]["type"]  # 반환 타입에 대한 정보를 가져옴
    if return_type["_nodetype"] == "TypeDecl":
        # 만약 반환 타입이 TypeDecl이라면 실제 타입 정보는 더 깊게 중첩되어 있음
        return_type_name = return_type["type"]["names"][0]
    else:
        # 반환 타입이 IdentifierType인 경우에는 바로 접근 가능
        return_type_name = return_type["names"][0]

    # 파라미터 정보에 접근
    try:
        parameters = func["decl"]["type"]["args"]["params"]
        params_list = [f"({param['decl']['type']['type']['names'][0]} {param['decl']['name']})" for param in parameters]
        params_str = ", ".join(params_list) if params_list else "없음"
    except KeyError:
        params_str = "없음"

    # if문 개수 계산
    if_count = sum(1 for node in func["body"]["block_items"] if node["_nodetype"] == "If")

    print("반환 타입:", return_type_name)
    print("파라미터:", params_str)
    print("if문 개수:", if_count)
    print("=" * 30)
