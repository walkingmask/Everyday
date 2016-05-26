#include <stdio.h>
#include <string.h>

/*
 * get the greatest common divisor of x and y
 */
int gcd(int x, int y) {
    if (y == 0) return x;
    return gcd(y, x%y);
}

/*
 * get the least common multipleof x and y
 */
int lcm(int x, int y) {
    if ( (0 == x) || (0 == y) ) return 0;
    return ((x/ gcd(x, y)) * y);
}

/*
 * a simple addition of fraction
 * f1:  fraction1
 * f2:  fraction2
 * res: result
 * return: there is no reason now
 */
int fracadd(const char *f1, const char *f2, char *res) {

    int top1, top2, bot1, bot2, comm;
    sscanf(f1, "%d/%d", &top1, &bot1);
    sscanf(f2, "%d/%d", &top2, &bot2);

    // reducing
    if (bot1 != bot2) {
        comm = lcm(bot1, bot2);
        top1 = top1 * (comm / bot1);
        top2 = top2 * (comm / bot2);
        bot1 = bot2 = comm;
    }

    sprintf(res, "%d/%d", top1+top2, bot2);

    return 0;
}

/*
 * a simple subtraction of fraction
 * f1:  fraction1
 * f2:  fraction2
 * res: result
 * return: there is no reason now
 */
int fracsub(const char *f1, const char *f2, char *res) {

    int top1, top2, bot1, bot2, comm;
    sscanf(f1, "%d/%d", &top1, &bot1);
    sscanf(f2, "%d/%d", &top2, &bot2);

    // reducing
    if (bot1 != bot2) {
        comm = lcm(bot1, bot2);
        top1 = top1 * (comm / bot1);
        top2 = top2 * (comm / bot2);
        bot1 = bot2 = comm;
    }

    sprintf(res, "%d/%d", top1-top2, bot2);

    return 0;
}