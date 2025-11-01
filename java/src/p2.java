import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class p2 {
    static int N;
    static int E;
    static List<List<int[]>> graph = new ArrayList<>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());

        graph = new ArrayList<>();
        for (int i = 0; i <= N; i++) graph.add(new ArrayList<>());

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            graph.get(a).add(new int[]{b, c});
            graph.get(b).add(new int[]{a, c});
        }

        st = new StringTokenizer(br.readLine());
        int v1 = Integer.parseInt(st.nextToken());
        int v2 = Integer.parseInt(st.nextToken());

        int[] start_dij = dijkstra(1);
        int[] v1_dij = dijkstra(v1);
        int[] v2_dij = dijkstra(v2);

        int to_v1 = start_dij[v1];
        int v1_v2 = v1_dij[v2];
        int v2_last = v2_dij[N];

        int to_v2 = start_dij[v2];
        int v2_v1 = v2_dij[v1];
        int v1_last = v1_dij[N];

        final int INF = Integer.MAX_VALUE;

// v1→v2 경로
        int v1_to_v2 = to_v1 + v1_v2 + v2_last;
// v2→v1 경로
        int v2_to_v1 = to_v2 + v2_v1 + v1_last;

// 불가능한 구간이 포함된 경우
        if (to_v1 == INF || v1_v2 == INF || v2_last == INF) v1_to_v2 = INF;
        if (to_v2 == INF || v2_v1 == INF || v1_last == INF) v2_to_v1 = INF;

// 두 경로 중 최소값 선택
        int answer = Math.min(v1_to_v2, v2_to_v1);

// 결과 출력
        System.out.println(answer >= INF ? -1 : answer);


    }

    public static int[] dijkstra(int start){
        int[] dist = new int[N+1];
        boolean[] check = new boolean[N+1];

        Arrays.fill(dist, Integer.MAX_VALUE);

        PriorityQueue<List<Integer>> pq = new PriorityQueue<>(
                Comparator.comparingInt(a -> a.get(0))
        );
        pq.add(List.of(0, start));

        while (!pq.isEmpty()){
            List<Integer> next = pq.poll();
            if (check[next.get(1)]){
                continue;
            }

            check[next.get(1)] = true;
            List<int[]> next_graph = graph.get(next.get(1));
            int next_length = next.get(0);
            dist[next.get(1)] = next_length;

            for (int[] ng : next_graph){
                int length = ng[1];
                int to_go = ng[0];

                if (next_length + length < dist[to_go]) {
                    pq.add(List.of(next_length + length, to_go));
                }
            }

        }
        return dist;
    }
}