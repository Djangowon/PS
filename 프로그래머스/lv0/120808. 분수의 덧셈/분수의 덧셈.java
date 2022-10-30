class Solution {
    public int[] solution(int denum1, int num1, int denum2, int num2) {
        int[] answer = new int[2];
        answer[0] = denum1 * num2 + denum2 * num1;
        answer[1] = num1 * num2;
        
        int gcd = gcd(answer[0], answer[1]);
        
        answer[0] = answer[0] / gcd;
        answer[1] = answer[1] / gcd;
        
        return answer;
    }
    
    static int gcd(int a, int b) {
        if(a % b == 0) {
            return b;
        }
        return gcd(b, a % b);
    }
}