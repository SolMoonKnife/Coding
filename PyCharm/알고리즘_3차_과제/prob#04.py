def solution_04():
    class Person:
        def __init__(self, name, address, company, zipcode, phones, email):
            self.name = name
            self.address = address
            self.company = company
            self.zipcode = zipcode
            self.phones = phones
            self.email = email

        def get_name(self):
            return self.name

        def get_full_info(self):
            return (
                self.name,
                self.address,
                self.company,
                self.zipcode,
                self.phones,
                self.email
            )
    class Node:
        def __init__(self, name):
            self.name = name
            self.left = None
            self.right = None
    class Binary_search_tree:
        def __init__(self):
            self.root = None

        def insert(self, key):
            def _insert(root, name):
                if root is None:
                    return Node(name)

                if root.name < name:
                    root.left = _insert(root.right, name)
                elif root.name > name:
                    root.right = _insert(root.left, name)

                return root

            self.root = _insert(self.root, key)

        def search(self, name):
            def _search(root, name):
                if root is not None:
                    if root.name == name:
                        return root

                    if root.name < name:
                        return _search(root.right, name)
                    elif root.name > name:
                        return _search(root.left, name)
                else:
                    return None

            return _search(self.root, name)

        def delete(self, name):
            def _node_delete(node, parent):
                if node == self.root:
                    self.root = _delete(self.root)
                elif node == parent.left:
                    parent.left = _delete(node)
                else:
                    parent.right = _delete(node)

            def _delete(node):
                if not node.left and not node.right:
                    return None
                elif not node.left and node.right:
                    return node.right
                elif node.left and not node.right:
                    return node.left
                else:
                    begin = node.right
                    parent = None  # 없어도 되는데 참조 오류 떠서 추가함
                    while begin.left:
                        parent = begin
                        begin = begin.left
                    self.root.data = begin.data
                    if begin == node.right:
                        self.root.right = begin.right
                    else:
                        parent.left = begin.right
                    return self.root
                    



    with open("address_book2020.tsv", "r") as file: pass

