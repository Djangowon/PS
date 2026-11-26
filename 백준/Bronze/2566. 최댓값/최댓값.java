import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int max = -1;
        int maxRow = 0;
        int maxCol = 0;

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                int input = sc.nextInt();
                if (max < input) {
                    max = input;
                    maxRow = i + 1;
                    maxCol = j + 1;
                }
            }
        }

        System.out.println(max);
        System.out.print(maxRow + " " + maxCol);
    }
}