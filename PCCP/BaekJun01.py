# 팰린드롬수 : 뒤에서부터 읽어도 앞에서부터 읽은 것과 같은 수
# 입력받은 값이 팰린드롬수이면 'yes', 아니면 'no'를 출력하는 함수를 만들자.
# 앞에 무의미한 0은 올 수 없다고 정한다. 또한 마지막으로 0이 입력되면 반복이 종료된다.

# 구조 설계 : 스택에 전부 넣고 꺼내면서 역순으로 같은지 확인

def is_palindrome(num):
    # 숫자를 문자열로 변환하여 팰린드롬 여부를 확인하는 함수
    num_str = str(num)
    return num_str == num_str[::-1] # 역순으로 배열한 리스트와 비교하는 핵심 문장
    # 숫자를 문자열로 변환한 뒤 [::-1]을 취하면 간단히 역순으로 배열할 수 있다.

def main():
    numbers = []  # 입력된 정수를 저장할 리스트

    while True:
        input_num = input("정수를 입력하세요 (0 입력 시 종료): ")

        # 입력이 숫자이고 1부터 999999 사이의 수인지 확인
        if input_num.isdigit():
            num = int(input_num)
            if num == 0:
                break  # 0이 입력되면 반복문 종료
            elif 1 <= num <= 999999:
                numbers.append(num)
            else:
                print("1부터 999999 사이의 정수를 입력하세요.")
        else:
            print("올바른 정수를 입력하세요.")

    for num in numbers:
        result = 'yes' if is_palindrome(num) else 'no'
        print(result)


if __name__ == "__main__":
    main()
