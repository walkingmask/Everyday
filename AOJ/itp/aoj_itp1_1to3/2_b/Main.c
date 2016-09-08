
/*---
 * AOJ/ITP1/2_B/Main.c
 * 2015/02/27(FRI)
 * walkingmask
 * AIZU ONLINE JUDGE 練習用プログラム
 * http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_2_B
---*/

#include <stdio.h>

int main(){
        int i1, i2, i3;
        scanf("%d %d %d", &i1, &i2, &i3);
        if(i1 < i2 && i2 < i3)
                printf("Yes\n");
        else
                printf("No\n");
        return(0);
}

/*---
 * 出力結果
/2_B% ./Main 
1 3 8
Yes
/2_B% ./Main
3 8 2
No
---*/