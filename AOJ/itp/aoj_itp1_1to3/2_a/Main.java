
/*---
 * AOJ/ITP1/2_B/Main.java
 * 2015/03/11(WED)
 * walkingmask
 * AIZU ONLINE JUDGE 練習用プログラム
 * http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_2_B
---*/

import java.util.Scanner;

public class Main { 
	public static void main(String[] args){
		String str;
                int i1, i2;;
 
                Scanner scan = new Scanner(System.in);
 
                str = scan.next();
                i1 = Integer.parseInt(str);
         
                str = scan.next();
                i2 = Integer.parseInt(str);

                if     (i1<i2)
                	System.out.println("a < b");
                else if(i1>i2)
        	       System.out.println("a > b");
                else
        	       System.out.println("a == b");
	}
}

/*---
 * 出力結果
/2_B% java Main
1 2
a < b
/2_B% java Main
4 3
a > b
/2_B% java Main
4 4
a == b
---*/
