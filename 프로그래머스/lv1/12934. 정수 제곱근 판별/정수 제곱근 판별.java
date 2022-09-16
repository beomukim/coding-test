class Solution {
    public long solution(long n) {
        double tmp = Math.sqrt(n);
        if (tmp == Math.floor(tmp)) {
            return (long) ((tmp + 1) * (tmp + 1));
        } else {
            return -1;
        }
    }
}