import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class p1 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());

        int[] dp = new int[n+1];
        dp[0] = 1;
        dp[1] = 1;

        for(int i=2; i <= n; i++){
            int bef_one = dp[i-1];
            int bef_two = dp[i-2] * 2;
            int now = (bef_one + bef_two) % 10007;
            dp[i] = now;
        }
        System.out.println(dp[dp.length-1]);
    }
}