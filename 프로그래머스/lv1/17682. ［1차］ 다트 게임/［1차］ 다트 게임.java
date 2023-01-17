import java.util.*;

class Solution {
    public int solution(String s) {

        String[] number = s.split("S|D|T");
        Map<Integer, String> option = new HashMap<>();
        for (int i = 0; i < number.length; i++) {
            if (number[i].contains("#")) {
                option.put(i, "#");
            }
            if (number[i].contains("*")) {
                option.put(i, "*");
            }
        }
        int[] num = new int[3];
        for (int i = 0; i < 3; i++) {
            num[i] = Integer.parseInt(number[i].replaceAll("[^0-9]", ""));
        }
        ArrayList<Integer> pow = new ArrayList<>();
        StringTokenizer stringTokenizer = new StringTokenizer(s, "S|D|T",true);
        while (stringTokenizer.hasMoreTokens()) {
            String token = stringTokenizer.nextToken();
            if (token.equals("S")) {
                pow.add(1);
            }
            if (token.equals("D")) {
                pow.add(2);
            }
            if (token.equals("T")) {
                pow.add(3);
            }
        }
        int answer = 0;
        double[] term = new double[3];
        for (int i = 0; i < 3; i++) {
            term[i] = Math.pow(num[i], pow.get(i));
        }

        for (int i = 0; i < 3; i++) {
            if (option.get(i + 1) != null && option.get(i + 1).equals("*") && i > 0) {
                term[i] *= 2;
                term[i-1] *= 2;
            }
            if (option.get(i + 1) != null && option.get(i + 1).equals("*") && i == 0) {
                term[i] *= 2;
            }
            if (option.get(i + 1) != null && option.get(i + 1).equals("#")) {
                term[i] = -Math.abs(term[i]);
            }
        }

        for (int i = 0; i < term.length; i++) {
            answer += term[i];
        }
        return answer;
    }
}