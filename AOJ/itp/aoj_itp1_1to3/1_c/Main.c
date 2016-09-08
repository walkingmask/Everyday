
/*---
 * AOJ/ITP1/1_C/Main.c
 * 2015/02/27(FRI)
 * walkingmask
 * AIZU ONLINE JUDGE 練習用プログラム
 * http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_C
---*/

#include <stdio.h>
 
int main(){
   int i1 ,i2;
   scanf("%d %d", &i1, &i2);
   printf("%d %d\n", i1*i2, 2*(i1+i2));
   return(0);
}

/*---
 * 出力結果
 /1_C% ./Main   
12 32
384 88
---*/