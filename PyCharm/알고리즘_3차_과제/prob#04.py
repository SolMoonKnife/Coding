def solution_04():
    class Person:
        def __init__(self, name, address, company, zipcode, phones, email):
            self.name = name
            self.address = address
            self.company = company
            self.zipcode = zipcode
            self.phones = phones
            self.email = email

        def get_full_info(self):  # 현재 필요 없음
            return (
                self.name,
                self.address,
                self.company,
                self.zipcode,
                self.phones,
                self.email
            )

        def get_str(self):
            return (f"{self.name}\n"
                    f"  Company: {self.company}\n"
                    f"  Address: {self.address}\n"
                    f"  Zipcode: {self.zipcode}\n"
                    f"  Phones: {self.phones}\n"
                    f"  Email: {self.email}" )

        # 이진 탐색 트리의 key가 Person 객체이므로 key를 참조할 때 name을 확인할 수 있어야 한다
        def __lt__(self, other):
            return self.name < other.name
        def __eq__(self, other):
            return self.name == other.name
    class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None
    class Binary_search_tree:
        def __init__(self):
            self.root = None

        def insert(self, key):
            def _insert(node, key):
                if not node:
                    return Node(key)

                if key < node.key:
                    node.left = _insert(node.left, key)
                elif key > node.key:
                    node.right = _insert(node.right, key)

                return node

            self.root = _insert(self.root, key)

            return self.root is not None  # 삽입 성공 여부

        def search(self, key, trace=False):
            def _search(node, key, trace):
                if trace:
                    print(node.key.name)
                if not node:
                    return None
                # 키를 찾은 경우
                if node.key.name == key:
                    return node
                # 오른쪽 또는 왼쪽을 탐색해야 할 경우
                if node.key.name < key:
                    return _search(node.right, key, trace)
                else:
                    return _search(node.left, key, trace)

            return _search(self.root, key, trace)
        # search 함수에 매개 변수를 추가하여 trace 기능을 통합함.

        def delete(self, key):
            def _get_successor(node):
                min_key = node.key  # 최소 키 초기화
                while node.left:    # 최대한 왼쪽 노드로 이동 (우측 서브 트리 내에서)
                    min_key = node.left.key  # 왼쪽 노드가 존재하는 동안 왼쪽 키로 업데이트
                    node = node.left  # 다음 왼쪽 노드로 이동

                return min_key
                
            def _delete(node, key):
                if not node:
                    return None

                if key < node.key.name:          # 노드보다 키가 작으면 왼쪽으로 이동해서 지운다
                    node.left = _delete(node.left, key)  # ★ 그리고 지운 결과 서브 트리를 왼쪽 노드에 연결한다.
                elif key > node.key.name:
                    node.right = _delete(node.right, key)
                else:
                    if not node.left:       # 우선 한쪽 자식만 있는 경우를 처리
                        return node.right   # 자식이 하나만 있으면 그 자식을 끌어 올리면 됨
                    if not node.right:
                        return node.left

                    # 자식이 둘 있는 경우: 삭제 대상 노드의 키 값을 후계자 노드의 키 값으로 대체하고 후계자 노드를 삭제
                    #
                    node.key = _get_successor(node.right)  # 우측 서브 트리의 최소 키를 후계자 키로 선택 및 대체
                    node.right = _delete(node.right, node.key.name)  # 대체한 키 값을 사용하여 우측 서브 트리의 후계자 노드 삭제
            
                return node  # 삭제(후계자 대체) 작업이 완료된 node 반환

            self.root = _delete(self.root, key)
            # 1) root is None: None
            # 2) root has one chile: root.left OR root.right
            # 3) root has two children: replace key with successor's key and delete successor node

        def print_in_order(self):
            def _print_in_order(root):
                if root:
                    _print_in_order(root.left)
                    print(root.key.get_str())
                    _print_in_order(root.right)

            _print_in_order(self.root)

    people = Binary_search_tree()
    def read_file(file_name):
        with open(file_name, "r") as file:
            people_lines = file.readlines()

        for line in people_lines[1:]:  # 파일의 첫 줄을 제외합니다
            name, address, company, zipcode, phones, email = map(str.strip, line.split('\t'))  # 분할 및 공백 문자 제거 map
            people.insert(Person(name, address, company, zipcode, phones, email))  # 언팩된 필드를 바탕으로 객체를 생성해 삽입

    while True:
        order = tuple(map(str.strip, input().split()))
        if order[0] == "read":
            read_file(order[1])
        elif order[0] == "list":
            people.print_in_order()
        elif order[0] == "find":
            result = people.search(order[1])
            if result:
                print(result.key.get_str())
            else:
                print("Do not Found")
        elif order[0] == "delete":
            people.delete(order[1])
        elif order[0] == "trace":
            result = people.search(order[1], trace=True)
            if result:
                print(result.key.get_str())
            else:
                print("Do not Found")
        elif order[0] == "exit":
            break
        else:
            print("wrong order")


solution_04()
