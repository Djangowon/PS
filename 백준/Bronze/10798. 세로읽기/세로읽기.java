import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[][] matrix = new String[5][15];

        for (int i = 0; i < 5; i++) {
            String[] input = sc.nextLine().split("");

            for (int j = 0; j < input.length; j++) {
                matrix[i][j] = input[j];
            }
        }

        for (int col = 0; col < 15; col++) {
            for (int row = 0; row < 5; row++) {
                if (matrix[row][col] != null) {
                    System.out.print(matrix[row][col]);
                }
            }
        }

    }
}