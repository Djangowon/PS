class Solution {
    public int solution(String my_string) {
        int answer = 0;
        String[] strArray = my_string.split("");
        
        for (int i = 0; i < strArray.length; i++) {
            if (strArray[i].matches("-?\\d+")) {
                answer += Integer.parseInt(strArray[i]);
            }
        }
        return answer;
    }
}