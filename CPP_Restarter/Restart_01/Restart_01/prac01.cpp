#include <stdio.h>

int main(void) {
	int Num1, Num2;
	int Sum = 0;
	int i;

	printf("2���� ���� �Է�: ");
	scanf_s("%d %d", &Num1, &Num2);

	for (i = Num1; i <= Num2; i++) {
		Sum += i;
	}
	printf("%d���� %d������ ��: %d", Num1, Num2, Sum);

	return 0;
}