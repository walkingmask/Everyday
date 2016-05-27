/* fcalc.c
 * 2016/05/26(Thu)
 * walkingmask
 * discripthon
 *  Calculating remain fractional
 * ToDo
 *  ・分母が1の時は整数値を出力する
 *  ・整数値との複合計算
 */

#include <stdio.h>
#include <string.h>
#include "frac.h" // the special header

int main(int argc, char *argv[]) {

    // Usage
    if (argc != 2) {
        fprintf(stderr, "Usage   : fcalc \"frac1 op frac2\"\n");
        fprintf(stderr, "example : fcalc \"1/2 * 3/4\"\n");
        exit(EXIT_FAILURE);
    }

    // calculating
    char res[32];
    frac(argv[1], res);

    // output the result
    printf("%s\n", res);

    return 0;
}