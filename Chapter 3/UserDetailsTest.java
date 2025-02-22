import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class UserDetailsTest {

    private UserDetails userDetails;

    @BeforeEach
    public void setUp() {
        userDetails = new UserDetails("Alice", "123-456-7890", "alice@example.com", "123 Main St");
    }

    @Test
    public void testGetName() {
        assertEquals("Alice", userDetails.getName());
    }

    @Test
    public void testSetName() {
        userDetails.setName("Bob");
        assertEquals("Bob", userDetails.getName());
    }

    @Test
    public void testGetPhoneNumber() {
        assertEquals("123-456-7890", userDetails.getPhoneNumber());
    }

    @Test
    public void testSetPhoneNumber() {
        userDetails.setPhoneNumber("987-654-3210");
        assertEquals("987-654-3210", userDetails.getPhoneNumber());
    }

    @Test
    public void testGetEmailAddress() {
        assertEquals("alice@example.com", userDetails.getEmailAddress());
    }

    @Test
    public void testSetEmailAddress() {
        userDetails.setEmailAddress("bob@example.com");
        assertEquals("bob@example.com", userDetails.getEmailAddress());
    }

    @Test
    public void testGetHomeAddress() {
        assertEquals("123 Main St", userDetails.getHomeAddress());
    }

    @Test
    public void testSetHomeAddress() {
        userDetails.setHomeAddress("456 Elm St");
        assertEquals("456 Elm St", userDetails.getHomeAddress());
    }
}