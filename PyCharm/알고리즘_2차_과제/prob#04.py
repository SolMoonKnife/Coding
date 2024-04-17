import math

# 두 점 사이의 거리를 계산
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# 가장 가까운 두 점을 찾는 함수
def closest_pair(points):
    n = len(points)
    if n <= 1:
        return float('inf'), None, None
    elif n == 2:
        return distance(points[0], points[1]), points[0], points[1]

    # x좌표에 따라 정렬 <= O(nlogn)
    points.sort()

    # 분할 정복 기법: 가장 가까운 두 점
    mid = n // 2
    left_distance, left_point1, left_point2 = closest_pair(points[:mid])
    right_distance, right_point1, right_point2 = closest_pair(points[mid:])

    # 두 구간에서 찾은 최단 거리 중 최솟값
    min_distance = min(left_distance, right_distance)
    min_point1, min_point2 = None, None

    # 구간을 병합할 때 추가적으로 고려해야 하는 점들을 찾음
    strip = []
    for point in points:
        if abs(point[0] - points[mid][0]) < min_distance:
            strip.append(point)

    # 추가적으로 고려해야 하는 점들을 y좌표에 따라 정렬
    strip.sort(key=lambda x: x[1])

    # 추가적으로 고려해야 하는 점들에 대해 확인
    for i in range(len(strip)):
        for j in range(i + 1, min(i + 12, len(strip))):
            d = distance(strip[i], strip[j])
            if d < min_distance:
                min_distance = d
                min_point1, min_point2 = strip[i], strip[j]

    # 최종적인 최솟값을 반환
    if min_distance == left_distance:
        return min_distance, left_point1, left_point2
    elif min_distance == right_distance:
        return min_distance, right_point1, right_point2
    else:
        return min_distance, min_point1, min_point2


# 테스트를 위한 점들의 좌표
points = [(1, 2), (3, 5), (6, 1), (7, 8), (9, 10), (11, 14), (15, 18)]

# 최단 거리와 해당 점들을 출력
min_distance, point1, point2 = closest_pair(points)
print("최단 거리:", min_distance)
print("점1:", point1)
print("점2:", point2)
