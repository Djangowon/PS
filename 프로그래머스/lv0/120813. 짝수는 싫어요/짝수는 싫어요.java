class Solution {
    public int[] solution(int n) {
        int idx = 0;
        int[] answer = new int[n % 2 == 0 ? n / 2 : n / 2 + 1];
        for (int i = 1; i <= n; i++) {
            if (i % 2 != 0) {
                answer[idx] = i;
                idx += 1;
            }
        }
        return answer;
    }
}