class Solution {
    public static boolean isNumeric(String strNum) {
        if (strNum == null) {
            return false;
        }
        try {
            double d = Double.parseDouble(strNum);
        } catch (NumberFormatException nfe) {
            return false;
        }
        return true;
    }
    public int solution(String s) {
        if (isNumeric(s)) {
            return Integer.valueOf(s);
        } else {
            return Integer.valueOf(s.substring(1));
        }
    }
}