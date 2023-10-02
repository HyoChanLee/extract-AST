import json

json_data = """

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
