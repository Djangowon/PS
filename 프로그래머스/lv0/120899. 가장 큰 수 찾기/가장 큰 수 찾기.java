import java.util.Arrays;

class Solution {
    public int[] solution(int[] array) {
        int[] answer = new int[2];

        answer[0] = Arrays.stream(array).max().getAsInt();
        answer[1] =  Arrays.binarySearch(array, answer[0]);

        return answer;
    }
}