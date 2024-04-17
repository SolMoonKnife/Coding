# 후위 수열을 이진 검색 트리로 만들 수 있는가 확인
def solution_03():
    # [TESTCASE]
    post_01 = [2, 3, 4, 1, 8, 10, 9, 11, 7, 6]
    post_02 = [2, 3, 1, 4, 8, 10, 7, 11, 9, 6]
    post_03 = [2, 1, 4, 3, 5]
    post_04 = [1, 2, 3, 4, 5, 6, 7]
    post_05 = [1, 3, 5, 4, 2, 7, 8, 9, 11, 10, 12, 14, 16, 15, 13, 6]
    def isBinarySearchTree(post_list):
        # 이진 탐색 트리라면 중위 순회 결과는 정렬된 순열
        in_list = sorted(post_list)
        length = len(post_list)
        max_depth = 0

        def check_binary_tree(post_order, in_order, depth=0):
            nonlocal max_depth
            max_depth = max(depth, max_depth)
            if not post_order:
                return 0

            root = post_order[-1]

            if root not in in_order:
                return 0

            post_order.pop()
            index = in_order.index(root)
            
            # 후위 순열 : 반드시 우측부터 확인
            right = check_binary_tree(post_order, in_order[index + 1:], depth+1)
            left = check_binary_tree(post_order, in_order[:index], depth+1)

            return 1 + right + left
        
        # 후위 순열을 중위 순열과 조합하여 트리로 복원하는 과정이 정상적으로 끝났는 지 확인 (원본 길이와 비교)
        test = check_binary_tree(post_list, in_list)
        if test != length:
            return -1    # 비정상인 경우 -1을 반환
        return max_depth # 정상인 경우 최대 깊이를 반환

    print(isBinarySearchTree(post_01))
    print(isBinarySearchTree(post_02))
    print(isBinarySearchTree(post_03))
    print(isBinarySearchTree(post_04))
    print(isBinarySearchTree(post_05))

solution_03()