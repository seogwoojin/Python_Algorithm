import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class p_15903 {
    public static PriorityQueue<long[]> pq = new PriorityQueue<>(
            Comparator.comparingLong(a -> a[0])
    );

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] strings = br.readLine().split(" ");

        int N = Integer.parseInt(strings[0]);
        int M = Integer.parseInt(strings[1]);


        int[] cards = new int[N];
        String[] sc = br.readLine().split(" ");

        for (int i = 0; i < N; i++) {
            cards[i] = Integer.parseInt(sc[i]);
        }

        for (int i = 0; i < N; i++) {
            int card = cards[i];
            pq.add(new long[]{card, i});
        }

        for (int i=0; i<M; i++) {
            long[] first_card = pq.poll();
            long[] second_card = pq.poll();

            long sum = first_card[0] + second_card[0];

            pq.add(new long[]{sum, first_card[1]});
            pq.add(new long[]{sum, second_card[1]});
        }

        System.out.println(pq.stream().mapToLong(a->a[0]).sum());
    }
}