
/*---
 * AOJ/ITP1/1_D/Main.java
 * 2015/02/27(FRI)
 * walkingmask
 * AIZU ONLINE JUDGE 練習用プログラム
 * http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_D
---*/

public class Main { 
	public static void main(String[] args){
		// 秒数の読み込み
		int inSeconds = new java.util.Scanner(System.in).nextInt();
		// 出力する時間の計算
		int outHours = inSeconds / (60*60);
		// 出力する分数の計算
		inSeconds = inSeconds % (60*60);
		int outMinutes = inSeconds / 60;
		// 出力する秒数の計算
		inSeconds = inSeconds % 60;
		int outSeconds = inSeconds;
		// 出力
		System.out.println(outHours + ":" +outMinutes + ":" + outSeconds);
	}
}

/*---
 * 出力結果
/1_D% java Main
46979
13:2:59
---*/