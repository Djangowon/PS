class Solution {
    public int solution(int n) {
        double result = Math.sqrt(n);
        return result % 1 == 0 ? 1 : 2;
    }
}