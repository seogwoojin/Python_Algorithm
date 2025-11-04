import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Deque;
import java.util.List;
import java.util.StringTokenizer;

public class p6 {
    private static int[][] check;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine()); // 테스트 케이스 수



        for (int t = 0; t < T; t++) {
            int answer = 0;
            int K = Integer.parseInt(br.readLine()); // 장의 수
            int[] files = new int[K];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < K; i++) {
                files[i] = Integer.parseInt(st.nextToken());
            }

            check = new int[K][K];

            answer = dp(0, K-1, files);
            System.out.println(answer);
        }



    }

    private static int dp(int start, int end, int[] files){
        if (check[start][end] != 0){
            return check[start][end];
        }

        if (start == end) {
            return 0;
        } else {
            int dp_answer = Integer.MAX_VALUE;
            int sum = 0;
            for(int i=start; i<=end; i++){
                sum += files[i];
            }

            for(int i=start; i<end; i++){
                int left = dp(start, i, files);
                int right = dp(i+1, end, files);


                int temp = left + right + sum;

                if (temp < dp_answer) {
                    dp_answer = temp;
                }
            }
            check[start][end] = dp_answer;

            return dp_answer;
        }
    }
}