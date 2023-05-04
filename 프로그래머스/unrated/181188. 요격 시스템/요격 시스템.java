import java.util.Arrays;

class Solution {
    public int solution(int[][] targets) {
        int answer = 0;
        Arrays.sort(targets, (a, b) -> {
            if (a[1] == b[1]) {
                return a[0] - b[0];
            } else {
                return a[1] - b[1];
            }
        });

        int s = 0, e = 0;
        for (int[] target : targets) {
            if (target[0] >= e) {
                answer++;
                e = target[1];
            }
        }

        return answer;
    }
}
