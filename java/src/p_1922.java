import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class p_1922 {
    private static int[] check;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine()); // 컴퓨터 수
        int M = Integer.parseInt(br.readLine()); // 연결할 수 있는 선의 수

        int[][] edges = new int[M][3];
        for (int i = 0; i < M; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            edges[i][0] = Integer.parseInt(st.nextToken()); // a
            edges[i][1] = Integer.parseInt(st.nextToken()); // b
            edges[i][2] = Integer.parseInt(st.nextToken()); // c
        }

        check = new int[N+1];
        for (int i=1; i<N+1; i++) {
            check[i] = i;
        }

        Arrays.sort(edges, Comparator.comparingInt(a-> a[2]));

        int answer = 0;
        for (int[] edge : edges) {
            if (edge[0] == edge[1]) continue;

            int cost = edge[2];
            int edgeA = find(edge[0]);
            int edgeB = find(edge[1]);

            if (edgeA == edgeB) {
                continue;
            }

            check[edgeB]= edgeA;
            answer += cost;
        }
        System.out.println(answer);
        System.out.println();
    }

    static int find(int x){
        if (check[x] == x) {
            return x;
        }
        int root = find(check[x]);
        check[x] = root;
        return root;
    }
}