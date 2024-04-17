# '투포인터'를 이용하여 팰린드롬수를 판별하는 방식(while문 버전)
def is_palindrome(num):
    s = str(num)
    (left, right) = (0, len(s) - 1)
    # 왼쪽부터 인덱싱한 것과 오른쪽부터 인덱싱한 것
    
    while left < right:
        # 조건식 : 왼쪽 인덱스가 오른쪽 인덱스를 침범하면 종료
        if s[left] != s[right]:
            return False
            # 한 번이라도 같지 않으면 팰린드롬수가 아니므로 함수 종료
        (left, right) = (left + 1, right - 1)
    return True
    # while문을 정상적으로 탈출한 경우 True반환

def is_palindrome_for(num):
    s = str(num)
    for left in range(len(s)//2):
        # 홀수 개인 경우 중앙 인덱스를 무시하도록 정수 나눗셈을 사용해 left인덱싱
        right = -left - 1
        if s[left] != s[right]:
            return False
    return True

num = 12345
print(is_palindrome_for(num))
