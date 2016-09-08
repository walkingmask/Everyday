
/*---
 * AOJ/ITP1/2_C/Main.java
 * 2015/03/11(WED)
 * walkingmask
 * AIZU ONLINE JUDGE 練習用プログラム
 * http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_2_C
 * 参考URL : http://d.hatena.ne.jp/yaneurao/20091126
---*/

import java.util.Scanner;

public class Main { 
	public static void main(String[] args){
		String str;
                int[] arr = new int[3];
                int i, j, temp;
 
                // 3つの数値の読み込み
                Scanner scan = new Scanner(System.in);
                str = scan.next();
                arr[0] = Integer.parseInt(str);
                str = scan.next();
                arr[1] = Integer.parseInt(str);
                str = scan.next();
                arr[2] = Integer.parseInt(str);

                // selection sort
                for(i=1; i<3; i++){
                        temp = arr[i];
                        if(arr[i-1] > temp){
                                j = i;
                                do{
                                        arr[j] = arr[j-1];
                                        --j;
                                }while(j > 0 && arr[j-1] > temp);
                                arr[j] = temp;
                        }
                }

                System.out.println(arr[0] + " " + arr[1] + " " + arr[2]);
	}
}

/*---
 * 出力結果
/2_C% java Main
3 8 1
1 3 8
---*/
