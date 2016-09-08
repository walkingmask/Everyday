
/*---
 * AOJ/ITP1/1_C/Main.java
 * 2015/02/27(FRI)
 * walkingmask
 * AIZU ONLINE JUDGE 練習用プログラム
 * http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_C
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
 
        System.out.println(i1*i2 + " " + 2*(i1+i2));
	}
}

/*---
 * 出力結果
/1_C% java Main
12 32
384 88
---*/