#include <stdio.h>

int main(void) {
	int Num1, Num2;
	int Sum = 0;
	int i;

	printf("2개의 정수 입력: ");
	scanf_s("%d %d", &Num1, &Num2);

	for (i = Num1; i <= Num2; i++) {
		Sum += i;
	}
	printf("%d부터 %d까지의 합: %d", Num1, Num2, Sum);

	return 0;
}