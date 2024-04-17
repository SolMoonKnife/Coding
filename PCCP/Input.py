s = input()
print(type(s))
print(s)

# 인풋 안에 원하는 문자열을 적어서 유도 글귀를 바로 만들 수 있음
# 백준, SWEA -> 인풋 파트를 직접 정의해야 함
# ㄴ 인풋이 스트링일 수도 있으나 리스트 같은 것이 사용될 때도 있음
# Programers는 인풋을 따로 사용하지 않고 함수만 제출함

# 스트링 메서드 : split으로 토큰 분할
s_split = s.split()
print(s_split)
# split 메서드의 기본 구분자는 공백 문자

# 함수가 반복(순회) 가능한 자료형을 인자로 받을 경우 map함수를 사용해 각 요소를 캐스팅 가능
# map(int, mylist) -> map자료형으로 반환되며, list로 생성하면 각 요소가 int로 캐스팅된 리스트 반환됨
i_split = list(map(round, s_split))
print(i_split)
# 한 번에 캐스팅 불가능한 경우 ('1.1' -> 1) map을 바로 사용할 수는 없음