import org.apache.commons.text.StringEscapeUtils;

public class SecureUserRegistration {

    public void registerUser(HttpServletRequest request) {
        String username = request.getParameter("username");
        if (username == null || username.trim().isEmpty()) {
            throw new IllegalArgumentException("Username cannot be null or empty");
        }
        username = StringEscapeUtils.escapeHtml4(username); // Sanitize input to prevent XSS
    }
}