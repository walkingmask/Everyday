
/*---
 * AOJ/ITP1/3_D/Main.java
 * 2015/04/06(MON)
 * walkingmask
 * AIZU ONLINE JUDGE 練習用プログラム
 * http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_3_D
---*/

import java.util.Scanner;

public class Main {
	public static void main(String[] args){
                Scanner scan = new Scanner(System.in);
                int iNumA = scan.nextInt();
                int iNumB = scan.nextInt();
                int iNumC = scan.nextInt();
                int count = 0;
                for(int i=iNumA; i<=iNumB; i++){
                	if(iNumC%i == 0)
                		count++;
                }
                System.out.println(count);
	}
}

/*---
 * 出力結果
/3_D% java Main 
5 14 80
3
---*/
