import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Scanner;

public class TestVuln {
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter username: ");
        String user = scanner.nextLine();

        Connection conn = DriverManager.getConnection("jdbc:h2:mem:testdb", "sa", "");
        Statement stmt = conn.createStatement();
        stmt.execute("CREATE TABLE users (username VARCHAR(50), password VARCHAR(50))");
        stmt.execute("INSERT INTO users VALUES ('admin', 'adminpass')");

        // Vulnerable to SQL Injection
        String query = "SELECT * FROM users WHERE username = '" + user + "'";
        ResultSet rs = stmt.executeQuery(query);

        if (rs.next()) {
            System.out.println("User found: " + rs.getString("username"));
        } else {
            System.out.println("User not found.");
        }

        rs.close();
        stmt.close();
        conn.close();
        scanner.close();
    }
}