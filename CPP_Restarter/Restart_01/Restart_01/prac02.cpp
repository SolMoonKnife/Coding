#include <stdio.h>

int main(void) {
	double doubleNumber01, doubleNumber02;
	while (1) {
		printf("2개의 실수를 입력: ");
		scanf_s("%lf %lf", &doubleNumber01, &doubleNumber02);

		if (-0.000001 < doubleNumber02 && doubleNumber02 < 0.000001) break;
		else {
			printf("%lf + %lf = %lf\n", doubleNumber01, doubleNumber02, doubleNumber01 + doubleNumber02);
			printf("%lf - %lf = %lf\n", doubleNumber01, doubleNumber02, doubleNumber01 - doubleNumber02);
			printf("%lf * %lf = %lf\n", doubleNumber01, doubleNumber02, doubleNumber01 * doubleNumber02);
			printf("%lf / %lf = %lf\n", doubleNumber01, doubleNumber02, doubleNumber01 / doubleNumber02);
		}
	}

	return 0;
}