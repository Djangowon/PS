import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        int[] baskets = new int[n];

        for (int count = 0; count < m; count++) {
            int i = sc.nextInt();
            int j = sc.nextInt();
            int k = sc.nextInt();

            for (int index = i; index <= j; index++) {
                baskets[index-1] = k;
            }
        }

        for (int ball: baskets) {
            System.out.print(ball + " ");
        }
    }
}