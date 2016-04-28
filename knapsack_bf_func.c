/* knapsack_bf_func.c
 * 2016/04/28(Thu)
 * walkingmask
 * discripthon
 *  ビット演算とunsigned long long型を使って
 *   64個の組み合わせブルートフォースをする関数
 *    ファイル読み込みと個数指定オプションを実装
 * notice
 *  コンパイル時に -Ofast オプションを指定すること
 * note
 *  関数側でファイル制御するかmainでするか
 */

#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <sys/time.h>
#include <stdint.h>
#include <limits.h>

typedef struct {
	int weight;
	int value;
} ITEM;


// 引数: ファイル名filename, ファイルのスタート位置spos, itemの数n, 上限値limit
// 返値: 最適組み合わせビット列(int)
int knapsack_bf (char *filename, int spos, int n, int limit)
{
	// open the file
	FILE *fp;
	if ((fp = fopen(filename, "r")) == NULL) {
		printf("file open error!!\n");
		exit(EXIT_FAILURE);
	}

	// init the items array
	ITEM items[n];
	int i;

	// skiping
	char buf[256];
	for (i=1; i<spos; i++) {
		if (fgets(buf, 256, fp) == NULL) break;
	}

	for (i=0; i<n; i++) {
		if (fscanf(fp, "%d,%d", &items[i].weight, &items[i].value) == EOF) break;
	}

	fclose(fp);

	unsigned long long c, count, res_count;
	int sumw, sumv, bin, res_sumv, res_sumw;

	for (count=res_count=1, res_sumv=0, c=-1; 0<count && count<=(c>>(64-n)); count++) {
		for (i=sumw=sumv=0, bin=1; i<n; i++, bin*=2) {
			if ((count & bin) == bin) {
				sumw += items[i].weight;
				sumv += items[i].value;
			}
		}
		if (sumw <= limit && sumv > res_sumv) {
			res_sumv = sumv;
			res_sumw = sumw;
			res_count = count;
		}
		// progress
		printf("\rprogress %lluman: v=%d, w=%d", count/10000, res_sumv, res_sumw);
	}
	printf("\n");

	// resulet
	for (i=0, bin=1; i<n; i++, bin*=2){
		if ((res_count & bin) == bin) printf("(%d, %d) ", items[i].weight, items[i].value);
	}
	printf("\nresult: w=%d, v=%d\n", res_sumw, res_sumv);

	return 0;
}

// 引数: Usage参照
int main (int argc, char *argv[])
{
	// Usage
	if (argc < 5) {
		printf("Usage: ./func [FILE_NAME] [START_POSITION] [N] [LIMIT]\n");
		exit(EXIT_FAILURE);
	}

	// check the arguments
	int spos, n, limit;
	spos  = atoi(argv[2]);
	n     = atoi(argv[3]);
	limit = atoi(argv[4]);
	if (spos == 0 || spos < 0) {
		printf("unexpected argument: %s\n", argv[2]);
		exit(EXIT_FAILURE);
	}
	if (n == 0 || n < 0 || n > 64) {
		printf("unexpected argument: %s\n", argv[3]);
		exit(EXIT_FAILURE);
	}
	if (limit == 0 || limit < 0) {
		printf("unexpected argument: %s\n", argv[4]);
		exit(EXIT_FAILURE);
	}

	knapsack_bf(argv[1], spos, n, limit);

	return 0;
}

