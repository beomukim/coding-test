import java.util.ArrayList;

class Solution {
    public long[] solution(int x, int n) {
        ArrayList<Long> answer = new ArrayList<>();
        for (long i = 1; i <= n; i++) {
            answer.add(x * i);
        }
        long[] array = new long[answer.size()];
        int size = 0;
        for (long r : answer) {
            array[size++] = r;
        }
        return array;
    }
}