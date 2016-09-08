
/*---
 * AOJ/ITP1/2_A/Main.java
 * 2015/02/27(FRI)
 * walkingmask
 * AIZU ONLINE JUDGE 練習用プログラム
 * http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_2_A
---*/

import java.util.Scanner;

public class Main { 
	public static void main(String[] args){
        // 変数と配列
	String str;
        int inNumber1, inNumber2, inNumber3;
 
        // 各数字の入力
        Scanner scan = new Scanner(System.in);
        str = scan.next();
        inNumber1 = Integer.parseInt(str);
        str = scan.next();
        inNumber2 = Integer.parseInt(str);
        str = scan.next();
        inNumber3 = Integer.parseInt(str);

        // 条件判定
        if(inNumber1 < inNumber2 && inNumber2 < inNumber3)
                System.out.println("Yes");
        else
                System.out.println("No");
	}
}

/*---
 * 出力結果
/2_A% java Main 
1 3 8
Yes
/2_A% java Main
3 8 2
No
---*/