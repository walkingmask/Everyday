/* aoj_itp1_4_b.c
 * 2016/04/29(Fri)
 * walkingmask
 */

#include <stdio.h>

int main(int argc, char *argv[])
{
	double r, pi;
	pi = 3.14159265359;
	scanf("%lf", &r);
	printf("%lf %lf\n", pi*r*r, 2*pi*r);
	return 0;
}