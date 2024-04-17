# N개의 노드를 가진 이진 트리가 다음과 같은 방식으로 주어진다.
# 인덱스 번호가 노드 번호인 수열이 주어진다. (0 ~ N-1)
# 수열의 값은 부모 노드의 번호이다.
# 값이 -1이면 루트 노드이다.

class Tree:
    def __init__(self, node, left=None, right=None):
        self.node = node
        self.left = left
        self.right = right

test = [1, 5, 5, 2, 2, -1, 3]

ref = [[] for _ in range(len(test))]  # 해당 번호 노드의 자식들을 저장
rootnum = -1

# 특정 노드의 자식 노드 정보를 매핑
for i, v in enumerate(test):
    if v != -1:
        ref[v].append(i)
    else:
        rootnum = i

tree = []
# 모든 노드 생성
for i in range(len(ref)):
    tree.append(Tree(i))

# 각 노드에 자식 노드 정보 연결
for i, child in enumerate(ref):
    if child:
        tree[i].left = tree[child.pop(0)]
        if child:
            tree[i].right = tree[child.pop()]
            
root = tree[rootnum]  # 루트 노드 연결

def preOrder(node):
    if node is not None:
        print(node.node, end=' ')
        preOrder(node.left)
        preOrder(node.right)

def inOrder(node):
    if node is not None:
        inOrder(node.left)
        print(node.node, end=' ')
        inOrder(node.right)

def postOrder(node):
    if node is not None:
        postOrder(node.left)
        postOrder(node.right)
        print(node.node, end=' ')

print("pre odder:")
preOrder(root)
print("\nin order:")
inOrder(root)
print("\npost order:")
postOrder(root)
