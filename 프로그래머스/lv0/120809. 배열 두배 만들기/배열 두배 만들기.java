class Solution {
    public int[] solution(int[] numbers) {
        int idx = 0;
        int[] answer = new int[numbers.length];
        for (int number : numbers) {
            answer[idx] = number * 2;
            idx += 1;
        }
        return answer;
    }
}