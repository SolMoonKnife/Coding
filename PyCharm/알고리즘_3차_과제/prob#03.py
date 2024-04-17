# 후위 순회 수열을 전위 순회 수열로 바꾸어 출력하라. (이진 탐색 트리)
# 수열의 길이 N과 후위 순회 수열에 해당하는 N개의 정수가 주어진다.

# 전위 순회 수열이면 루트를 확인한 다음 왼쪽, 오른쪽 순서로 탐색한다.

def solution_03():
    class Tree:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def build_binary_tree(post_order):
        in_order = sorted(post_order)

        def helper(post_order, in_order):
            if not post_order:
                return None

            root_value = post_order[-1]
            if root_value not in in_order:
                return None

            post_order.pop()
            index = in_order.index(root_value)

            root = Tree(root_value)
            root.right = helper(post_order, in_order[index+1:])
            root.left = helper(post_order, in_order[:index])

            return root

        return helper(post_order, in_order)

    def print_pre_order(root):
        if root:
            print(root.data, end=' ')
            print_pre_order(root.left)
            print_pre_order(root.right)

    while True:
        N = int(input())
        if N == -1:
            break
        post_order = list(map(int, input().split()))

        print_pre_order(build_binary_tree(post_order))
        print()

solution_03()  # N으로 -1을 입력하면 종료됩니다
