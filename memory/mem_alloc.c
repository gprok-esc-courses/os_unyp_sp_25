#include <stdio.h>
#include <stdlib.h>

int main() {
	int a = 5;
	int * p = &a;

	printf("Value of a is %d\n", a);
	printf("Address of a is %p\n", p);

	p = (int *)malloc(sizeof(int));
	printf("Address of dynamic allocation is %p\n", p);

	*p = 10;
	printf("Value of where p points to is %d\n", *p);

	// Deallocate p
	free(p);
}