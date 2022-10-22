class Solution {
    public int solution(int n) {
        int div = Math.floorDiv(n, 7);
        int mod = Math.floorMod(n, 7);
        
        if (mod > 0) {
            div += 1;
        }
        return div;
    }
}