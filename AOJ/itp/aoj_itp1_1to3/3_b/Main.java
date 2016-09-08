
/*---
 * AOJ/ITP1/3_B/Main.java
 * 2015/04/06(MON)
 * walkingmask
 * AIZU ONLINE JUDGE 練習用プログラム
 * http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_3_B
---*/

import java.util.Scanner;

public class Main {
	public static void main(String[] args){
                Scanner scan = new Scanner(System.in);
                for(int i=1; i>0; i++){
                        int iNum = scan.nextInt();
                        if(iNum == 0)
                                break;
                        System.out.println("Case " + i + ": " + iNum);
                }
	}
}

/*---
 * 出力結果
/3_B% java Main 
2
1
3
0
Case 1: 2
Case 2: 1
Case 3: 3
---*/