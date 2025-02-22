public class PasswordUtil {

    public static String hashPassword(String password) {
        // Implement a simple hashing mechanism (e.g., using SHA-256)
        // Note: In a real application, consider using a stronger hashing algorithm and salting.
        return Integer.toHexString(password.hashCode());
    }

    public static boolean isPasswordValid(String rawPassword, String hashedPassword) {
        // Validate the password by comparing the hashed version of the raw password
        return hashPassword(rawPassword).equals(hashedPassword);
    }
}