
/*---
 * AOJ/ITP1/3_C/Main.java
 * 2015/04/06(MON)
 * walkingmask
 * AIZU ONLINE JUDGE 練習用プログラム
 * http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_3_C
---*/

import java.util.Scanner;

public class Main {
	public static void main(String[] args){
                Scanner scan = new Scanner(System.in);
                for(int i=1; i>0; i++){
                        int iNum1 = scan.nextInt();
                        int iNum2 = scan.nextInt();
                        if(iNum1 == 0 && iNum2 == 0)
                                break;
                        if(iNum1 > iNum2){
                        	int temp = iNum1;
                        	iNum1 = iNum2;
                        	iNum2 = temp;
                        }
                        System.out.println(iNum1 + " " + iNum2);
                }
	}
}

/*---
 * 出力結果
/3_C% java Main 
3 2
2 2
5 3
0 0
2 3
2 2
3 5
---*/
