class Solution {
    public int[] solution(int n) {
        int[] arr = new int[10000];
        int idx =0;
       
        for(int i = 1; i<=n; i++) {
			if(n % i ==0) {
				arr[idx] = i;
				idx++;
			}
		}
        
		int[] answer = new int [idx];
		for(int i = 0; i < idx; i++) {
			if(arr[i] != 0) {
				answer[i] = arr[i];
			}
		}
        return answer;
    }
}