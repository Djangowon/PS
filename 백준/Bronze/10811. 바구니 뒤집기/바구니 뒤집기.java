import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] baskets = new int[n];
        int m = sc.nextInt();

        for (int i = 0; i < n; i++) {
            baskets[i] = i + 1;
        }
        for (int count = 0; count < m; count++) {
            int i = sc.nextInt();
            int j = sc.nextInt();

            int left = i - 1;
            int right = j - 1;

            while (left < right) {
                int temp = baskets[left];
                baskets[left] = baskets[right];
                baskets[right] = temp;

                left++;
                right--;
            }

        }
        for (int b: baskets) {
            System.out.print(b + " ");
        }
    }
}