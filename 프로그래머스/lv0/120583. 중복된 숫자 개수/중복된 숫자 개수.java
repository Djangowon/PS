class Solution {
    public int solution(int[] array, int n) {
        int count = 0;
        for (int number : array) {
            if (number == n) {
                count += 1;
            }
        }
        return count;
    }
}