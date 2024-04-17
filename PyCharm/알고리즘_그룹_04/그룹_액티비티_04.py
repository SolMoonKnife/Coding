def solution_04():
    post_order = [10, 9, 23, 22, 27, 25, 15, 50, 95, 60, 40, 29]
    in_order01 = [9, 10, 15, 22, 23, 25, 27, 29, 40, 50, 60, 95]
    in_order02 = [9, 10, 15, 22, 40, 50, 60, 95, 23, 25, 27, 29]
    in_order03 = [29, 15, 9, 10, 25, 22, 23, 27, 40, 60, 50, 95]
    in_order04 = [95, 50, 60, 40, 27, 23, 22, 25, 10, 9, 15, 29]

    class Tree:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def build_binary_tree(post_order, in_order):
        # post_order는 원본 리스트에서 직전 값이 제거된 것
        # in_order는 좌, 우 서브 트리로 슬라이싱된 것
        if not post_order:
            return None

        root = post_order[-1]

        if root not in in_order:
            return None

        post_order.pop()
        index = in_order.index(root)

        root_node = Tree(root)
        root_node.right = build_binary_tree(post_order, in_order[index+1:])  # 우측 서브 트리부터 확인
        root_node.left = build_binary_tree(post_order, in_order[:index])

        return root_node

    def print_in_order(root):
        if root:
            print_in_order(root.left)
            print(root.data, end=' ')
            print_in_order(root.right)

    tree01 = build_binary_tree(post_order.copy(), in_order01)
    tree02 = build_binary_tree(post_order.copy(), in_order02)
    tree03 = build_binary_tree(post_order.copy(), in_order03)
    tree04 = build_binary_tree(post_order.copy(), in_order04)

    print('1)', end=' ')
    print_in_order(tree01)
    print('\n2)', end=' ')
    print_in_order(tree02)
    print('\n3)', end=' ')
    print_in_order(tree03)
    print('\n4)', end=' ')
    print_in_order(tree04)

solution_04()
