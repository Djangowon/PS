import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        int[] baskets = new int[n];

        for (int i = 0; i < n; i++) {
            baskets[i] = i + 1;
        }

        for (int count = 0; count < m; count++) {
            int i = sc.nextInt();
            int j = sc.nextInt();

            int temp = baskets[i - 1];

            baskets[i - 1] = baskets[j - 1];
            baskets[j - 1] = temp;
        }

        for (int ball: baskets) {
            System.out.print(ball + " ");
        }

    }
}