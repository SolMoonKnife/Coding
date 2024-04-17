"""
출구까지 가는 경로 길이가 K이하인 서로 다른 경로의 개수를 계산하여라. (순환 이용)
경로의 길이는 이동 횟수를 의미하며, 같은 지점을 두 번 이상 방문할 수는 없다.
NN 미로에 대하여 출발점은 (0, 0)이고 도착점은 (N-1, N-1)이다.
경로의 개수 < 21억

미로 표현 방식: 이진 매트릭스 (0: way, 1: wall)
입력: 키보드로 입력받는다.
입력1: 미로 크기 N
입력N: 공백으로 구분된 미로의 각 행
입력N+1: 상수 K
"""

def numpath():
    # 입력 (N <= 16)
    N = 17
    while N > 16:
        N = int(input())

    # N개의 행을 공백 문자로 구분된 문자열로서 입력받아 이차원 배열 생성
    maze = []
    for i in range(N):
        maze.append(list(map(int, input().split(' '))))

    def pathfinder(x, y, moves):
        if (x < 0) or (y < 0) or (x > N-1) or (y > N-1) or maze[x][y] != 0:
            return False
        elif (x == N-1) and (y == N-1):
            return moves
        # ~패스 파인더 제작중~

    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

numpath()