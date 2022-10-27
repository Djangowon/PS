class Solution {
    public int solution(int price) {
        double totalPrice = price;

        if (100000 <= totalPrice && totalPrice < 300000 ) {
            totalPrice = totalPrice * 0.95;
        } else if (300000 <= totalPrice && totalPrice < 500000) {
            totalPrice = totalPrice * 0.9;
        } else if (500000 <= totalPrice) {
            totalPrice = totalPrice * 0.8;
        }
        return (int)totalPrice;
    }
}