import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;

public class p4 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());

        int[] houses = new int[N];
        for (int i = 0; i < N; i++) {
            houses[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(houses);

        List<Integer> gaps = new ArrayList<>();
        for (int i = 0; i< houses.length-1; i++){
            gaps.add(houses[i+1]-houses[i]);
        }

        int wants = gaps.size() - (C-1);

        for (int i = 0; i<wants; i++){
             List<Integer> idx = new ArrayList<>();
             int small = Integer.MAX_VALUE;

             for (int j = 0; j < gaps.size(); j++){
                 int gap = gaps.get(j);
                 if (gap < small){
                     small = gap;
                     idx = new ArrayList<>();
                     idx.add(j);
                 } else if(gap == small){
                     idx.add(j);
                 }
             }

             int[] choose = {0,Integer.MAX_VALUE, 0};

             for (int id : idx) {
                 if (id > 0){
                     int gap = gaps.get(id-1);
                     if (choose[1] > gap){
                         choose[0] = id-1;
                         choose[1] = gap;
                         choose[2] = id;
                     }
                 }

                 if (id < gaps.size()-1) {
                     int gap = gaps.get(id+1);
                     if (choose[1] > gap){
                         choose[0] = id + 1;
                         choose[1] = gap;
                         choose[2] = id;
                     }
                 }

             }

             int target;
             if (choose[0] > choose[2]){
                 target = choose[2];
             } else {
                 target = choose[0];
             }

             for (int j = 0; j < gaps.size(); j++) {
                 if (j == target) {
                     int sum = gaps.get(j)+gaps.get(j+1);
                     gaps.add(j, sum);
                     gaps.remove(j+1);
                     gaps.remove(j+1);
                 }
             }
        }

        System.out.println(gaps.stream().min(Integer::compareTo).get());
    }
}