class Solution {
    public int solution(String[] s1, String[] s2) {
        int answer = 0;
        for (String i : s2) {
            for (String j : s1) {
                if (j.equals(i)) {
                    answer += 1;
                }
            }
        }
        return answer;
    }
}