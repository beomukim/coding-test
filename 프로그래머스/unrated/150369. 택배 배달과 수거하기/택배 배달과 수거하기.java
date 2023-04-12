import java.util.*;
class Solution {
    public static long solution(int cap, int n, int[] deliveries, int[] pickups) {
    List<int[]> idps = new ArrayList<>();
    for (int i = 0; i < n; i++) {
        int d = deliveries[i];
        int p = pickups[i];
        if (d > 0 || p > 0) {
            int[] pair = new int[]{i+1, d, p};
            idps.add(pair);
        }
    }
    int delivery = 0;
    int pickup = 0;
    long answer = 0;
    while (!idps.isEmpty()) {
        int[] idp = idps.remove(idps.size()-1);
        int i = idp[0];
        int d = idp[1];
        int p = idp[2];
        delivery += d;
        pickup += p;
        while (delivery > 0 || pickup > 0) {
            delivery -= cap;
            pickup -= cap;
            answer += i*2;
        }
    }
    return answer;

    }
}