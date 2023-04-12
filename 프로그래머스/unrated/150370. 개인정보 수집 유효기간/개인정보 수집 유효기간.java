import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public static int[] solution(String today, String[] terms, String[] privacies) {
        List<Integer> answer = new ArrayList<>();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy.MM.dd");
        LocalDate dateTime = LocalDate.parse(today, formatter);

        Map<String, Integer> agreementTermsMap = new HashMap<>();

        for (String agreement : terms) {
            String[] parts = agreement.split(" ");
            String agreementName = parts[0];
            int retentionPeriod = Integer.parseInt(parts[1]);
            agreementTermsMap.put(agreementName, retentionPeriod);
        }

        for (int i = 0; i < privacies.length; i++) {
            String[] split = privacies[i].split(" ");
            long month = agreementTermsMap.get(split[1]);
            LocalDate parse = LocalDate.parse(split[0], formatter);
            LocalDate plusMonths = parse.plusMonths(month).minusDays(1L);
            if (plusMonths.isBefore(dateTime)) {
                answer.add(i+1);
            }

        }
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}