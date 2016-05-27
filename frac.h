#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
 * get the greatest common divisor of x and y
 */
int gcd(int x, int y) {
    if (y == 0) return x;
    return gcd(y, x%y);
}

/*
 * get the least common multiple of x and y
 */
int lcm(int x, int y) {
    if ( (0 == x) || (0 == y) ) return 0;
    return ((x/ gcd(x, y)) * y);
}

/*
 * do reduction
 */
void reduc(int *top, int *bot) {
    int comd;
    if ( (comd = abs( gcd(*top, *bot) )) != 1) {
        *top = *top / comd;
        *bot = *bot / comd;
    }
}

/*
 * a simple addition of fraction
 * f1     :  fraction1
 * f2     :  fraction2
 * res    : result
 * return : there is no reason now
 */
int fracadd(const char *f1, const char *f2, char *res) {

    int top1, top2, bot1, bot2, comm, rest, resb;
    sscanf(f1, "%d/%d", &top1, &bot1);
    sscanf(f2, "%d/%d", &top2, &bot2);

    // reducing
    if (bot1 != bot2) {
        comm = abs( lcm(bot1, bot2) );
        top1 = top1 * (comm / bot1);
        top2 = top2 * (comm / bot2);
        bot1 = bot2 = comm;
    }

    rest = top1 + top2;
    resb = bot1;
    reduc(&rest, &resb);

    sprintf(res, "%d/%d", rest, resb);

    return 0;
}

/*
 * a simple subtraction of fraction
 */
int fracsub(const char *f1, const char *f2, char *res) {

    int top1, top2, bot1, bot2, comm, rest, resb;
    sscanf(f1, "%d/%d", &top1, &bot1);
    sscanf(f2, "%d/%d", &top2, &bot2);

    // pre reducing
    if (bot1 != bot2) {
        comm = abs( lcm(bot1, bot2) );
        top1 = top1 * (comm / bot1);
        top2 = top2 * (comm / bot2);
        bot1 = bot2 = comm;
    }

    rest = top1 - top2;
    resb = bot1;
    reduc(&rest, &resb);

    sprintf(res, "%d/%d", rest, resb);

    return 0;
}

/*
 * a simple multiplication of fraction
 */
int fracmult(const char *f1, const char *f2, char *res) {

    int top1, top2, bot1, bot2, rest, resb;
    sscanf(f1, "%d/%d", &top1, &bot1);
    sscanf(f2, "%d/%d", &top2, &bot2);

    // pre reduction
    reduc(&top1, &bot2);
    reduc(&top2, &bot1);

    rest = top1 * top2;
    resb = bot1 * bot2;
    reduc(&rest, &resb);

    sprintf(res, "%d/%d", rest, resb);

    return 0;
}

/*
 * a simple division of fraction
 */
int fracdiv(const char *f1, const char *f2, char *res) {

    int top, bot;
    char tempf[16];

    // reverse the fraction 2
    sscanf(f2, "%d/%d", &top, &bot);
    sprintf(tempf, "%d/%d", bot, top);

    // multiplication
    fracmult(f1, tempf, res);

    return 0;
}

/*
 * fraction calculator
 * f     :   fomula of fraction
 * fomula must be like this "1/2 * 3/4"
 */
int frac(const char *f, char *res) {

    char tempf[32], *f1, *op, *f2;

    // convert const char* to char*
    strcpy(tempf, f);

    // get the fractions and operator from fomula
    f1 = strtok(tempf, " ");
    op = strtok(NULL, " ");
    f2 = strtok(NULL, " ");

    // switching the operation
    switch (*op) {
        case '+':
            fracadd(f1, f2, res);
            break;
        case '-':
            fracsub(f1, f2, res);
            break;
        case '*':
            fracmult(f1, f2, res);
            break;
        case '/':
            fracdiv(f1, f2, res);
            break;
        default:
            break;
    }

    return 0;
}