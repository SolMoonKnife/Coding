def solution_04():
    post_order = [10, 9, 23, 22, 27, 25, 15, 50, 95, 60, 40, 29]
    in_order = [29, 15, 9, 10, 25, 22, 23, 27, 40, 60, 50, 95]

    class Tree:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def build_binary_tree(post_order, in_order):
        # post_order는 원본 리스트에서 직전 값이 제거된 것
        # in_order는 좌, 우 서브 트리로 슬라이싱된 것



solution_04()