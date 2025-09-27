import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<String> names = new ArrayList<>();

        System.out.println("Enter the number of names:");
        int count = 0;
        while (true) {
            try {
                count = Integer.parseInt(scanner.nextLine());
                if (count > 0) {
                    break;
                } else {
                    System.out.println("Please enter a positive number:");
                }
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a valid number:");
            }
        }

        for (int i = 0; i < count; i++) {
            System.out.println("Enter name #" + (i + 1) + ":");
            String name = scanner.nextLine();
            names.add(name);
        }

        Collections.sort(names);

        // Introducing a logical error - division by zero
        int result = count / (count - count);  // This will throw ArithmeticException

        System.out.println("Sorted names:");
        for (String name : names) {
            System.out.println(name);
        }
        // Resource leak: scanner is not closed
    }
}