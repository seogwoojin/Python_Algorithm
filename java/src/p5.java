import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Deque;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.StringTokenizer;

public class p5 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine()); // 보드 크기
        int K = Integer.parseInt(br.readLine()); // 사과 개수

        int[][] board = new int[N + 1][N + 1]; // 1-indexed
        for (int i = 0; i < K; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            board[r][c] = 1; // 사과 표시
        }

        int L = Integer.parseInt(br.readLine());
        List<int[]> turns = new ArrayList<>();
        for (int i = 0; i < L; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int X = Integer.parseInt(st.nextToken());
            char C = st.nextToken().charAt(0);
            turns.add(new int[]{X, C});
        }


        List<int[]> dirs = new ArrayList<>();
        dirs.add(new int[]{0,1});
        dirs.add(new int[]{1,0});
        dirs.add(new int[]{0,-1});
        dirs.add(new int[]{-1,0});

        int dir_loc = 0;
        Deque<int[]> dq = new ArrayDeque<>();
        dq.add(new int[]{1,1});
        board[1][1] = -1;
        int time = 1;

        for (int[] turn : turns) {
            boolean break_flag = false;
            int[] move = dirs.get(dir_loc);
            for (int i = time; i <= turn[0]; i++){
                int[] head = dq.getFirst();
                int[] next_head = new int[]{head[0]+move[0], head[1]+move[1]};


                if (next_head[0] < 1 || next_head[0] > N ||  next_head[1] < 1 || next_head[1] > N){
                    break_flag = true;
                    break;
                }

                int next_board = board[next_head[0]][next_head[1]];

                if (next_board == -1){
                    break_flag = true;
                    break;
                }

                // 사과 존재 경우
                if (next_board == 1) {
                    dq.addFirst(next_head);
                } else {
                    dq.addFirst(next_head);
                    int[] last = dq.removeLast();
                    board[last[0]][last[1]] = 0;
                }
                board[next_head[0]][next_head[1]] = -1;
                time += 1;
            }

            if (break_flag) {
                break;
            }

            if (turn[1] == 'D'){
                dir_loc = (dir_loc + 1) % 4;
            } else {
                dir_loc = dir_loc - 1;
                if (dir_loc < 0) {
                    dir_loc = 3;
                }
            }
        }
        int[] move = dirs.get(dir_loc);
        while (true) {
            int[] head = dq.getFirst();
            int[] next_head = new int[]{head[0]+move[0], head[1]+move[1]};

            if (next_head[0] < 1 || next_head[0] > N ||  next_head[1] < 1 || next_head[1] > N){
                break;
            }

            int next_board = board[next_head[0]][next_head[1]];

            if (next_board == -1){
                break;
            }

            // 사과 존재 경우
            if (next_board == 1) {
                dq.addFirst(next_head);
            } else {
                dq.addFirst(next_head);
                int[] last = dq.removeLast();
                board[last[0]][last[1]] = 0;
            }
            board[next_head[0]][next_head[1]] = -1;
            time += 1;
        }
        System.out.println(time);

    }
}