/* knapsack_bf8.c
 * 2016/04/26(Tue)
 * walkingmask
 * discripthon
 *  ビット演算を使ってナップザック問題(8個だけ)
 * note
 *  最適化使うことで高速化できる
 *   メインforの中のforで
 *    bin計算を繰り返しているし
 *     iも64回しかないから
 *      ロープアンローリングした方が
 *     　64 * 2 * ULLONG_MAX だけ計算量が減る
 *  それともその程度の最適化はデフォルトでしてくれてる？
 *   => 検証
 *       最適化なし: 23msec
 *       最適化あり:  4msec
 */

#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <limits.h>

typedef struct {
	int weight;
	int value;
} ITEM;

#define WLIMIT 26 // ここの値を変える

int main(int argc, char *argv[])
{
	// variables
	ITEM item[] = {{3, 100}, {4, 80}, {9, 200}, {1, 80}, {3, 120}, {6, 180}, {5, 210}, {5, 220}}; // こいつもいじれる
	unsigned char count, res_count;
	int sumw, sumv, i, bin, res_sumv, res_sumw;

	clock_t start, stop;
	start = clock();

	for (count=res_count=1, res_sumv=0; 0<count && count<=UCHAR_MAX; count++) {
		for (i=sumw=sumv=0, bin=1; i<8; i++, bin*=2) {
			if ((count & bin) == bin) {
				sumw += item[i].weight;
				sumv += item[i].value;
			}
		}
		if (sumw <= WLIMIT && sumv > res_sumv) {
			res_sumv = sumv;
			res_sumw = sumw;
			res_count = count;
		}
	}

	stop = clock();
	printf("%lumsec\n", stop-start);

	// resulet
	for (i=0, bin=1; i<8; i++, bin*=2){
		if ((res_count & bin) == bin) printf("(%d, %d) ", item[i].weight, item[i].value);
	}
	printf("\nresult: w=%d, v=%d\n", res_sumw, res_sumv);

	return 0;
}
