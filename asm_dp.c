/* asm_dp.c
 * 2016/04/26(Tue)
 * walkingmask
 *
 * 説明
 * DPを使って2つの単語の相違度を求めるプログラム
 * Approximate string matching
 * 認知工学の理論入門 p24 宿題3 (1),(2)
 * 少し冗長なコードがある
 *   g(1,j),g(i,1)以外はifの演算いらないとか
 *   データ型が無駄にでかいとか
 * 
 *  argv[1] = "abcde" = I
 *  argv[2] = "abaf"  = J
 *
 *  i  e	0   1   0   1
 *     d	1   0   1   1
 *  ^  c	1   1   1   1
 *  |  b	1   1   1   1
 *     a	1   1   1   1
 *     0,0	a	b	a	f
 *
 *      	->		j
 *  i: 行, j: 列　(よく忘れる)
 */

#include <stdio.h>
#include <string.h>

int min_f(int a, int b, int c)
{
	if (a <= b && a <= c) return a;
	if (b <= a && b <= c) return b;
	return c;
}

int main(int argc, char *argv[])
{
	// usage
	if (argc != 3) {
		printf("Usage: ./dp word1 word2\n");
		return 1;
	}

	int I = strlen(argv[1]), J = strlen(argv[2]);
	int i, j;

	// d matrix
	int d[I][J];
	for (i=0; i<I; i++) {
		for (j=0; j<J; j++) {
			d[i][j] = (argv[1][i] != argv[2][j])? 1 : 0;
		}
	}

	// print d matrix
	printf("d matrix\n");
	printf("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n");
	for (i=I-1; i>=0; i--){
		printf("%c", argv[1][i]);
		for (j=0; j<J; j++){
			printf("\t%d", d[i][j]);
		}
		printf("\n");
	}
	printf("\n");
	for (j=0; j<J; j++) printf("\t%c", argv[2][j]);
	printf("\n\n");

	// g matrix
	int g[I][J], t1, t2, t3;
	g[0][0] = 2 * d[0][0];
	for (i=0; i<I; i++) {
		for (j=0; j<J; j++) {
			 t1 = t2 = t3 = I*J;
			if (i-1 >= 0 )
				t1 = g[i-1][j] + d[i][j];
			if (i-1 >= 0 && j-1 >= 0)
				t2 = g[i-1][j-1] + 2 * d[i][j];
			if (j-1 >= 0 )
				t3 = g[i][j-1] + d[i][j];
			g[i][j] = (i==0 && j==0)? g[i][j] : min_f(t1, t2, t3);
		}
	}

	// print g matrix
	printf("g matrix\n");
	printf("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n");
	for (i=I-1; i>=0; i--){
		printf("%c", argv[1][i]);
		for (j=0; j<J; j++){
			printf("\t%d", g[i][j]);
		}
		printf("\n");
	}
	printf("\n");
	for (j=0; j<J; j++) printf("\t%c", argv[2][j]);
	printf("\n\n");

	// answer
	printf("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n");
	printf("answer => %d\n", g[I-1][J-1]);

	return 0;
}

