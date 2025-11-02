import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class p3 {
    static int N;
    static int E;
    static List<List<int[]>> graph = new ArrayList<>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String s = st.nextToken();

        StringBuilder sb = new StringBuilder();
        int answer = 0;
        boolean plus = true;

        for (int i=0; i < s.length(); i++){
            char ch = s.charAt(i);
            if (ch == '+' || ch == '-'){
                if (plus){
                    answer += Integer.parseInt(sb.toString());
                } else {
                    answer -= Integer.parseInt(sb.toString());
                }

                if (ch == '-'){
                    plus = false;
                }


                sb = new StringBuilder();
            } else {
                sb.append(ch);
            }
        }
        if (plus){
            answer += Integer.parseInt(sb.toString());
        } else {
            answer -= Integer.parseInt(sb.toString());
        }

        System.out.println(answer);
    }
}