class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        
        String[] enableWords = {"aya", "ye", "woo", "ma"};
        String[] unableWords = {"ayaaya", "yeye", "woowoo", "mama"};
        
        for (String str : babbling) {
            String tempStr = str;

            for (String unableWord : unableWords) {
                tempStr = tempStr.replace(unableWord, "x");
            }
            for (String enableWord : enableWords) {
                tempStr = tempStr.replace(enableWord, "");
            }
            if (tempStr.length() == 0) {
                answer++;
            }
        }
        return answer;
    }
}