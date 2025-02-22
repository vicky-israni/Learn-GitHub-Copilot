

public class UserDetails {
    private String name;
    private String phoneNumber;
    private String emailAddress;
    private String homeAddress;

    public UserDetails(String name, String phoneNumber, String emailAddress, String homeAddress) {
        this.name = name;
        this.phoneNumber = phoneNumber;
        this.emailAddress = emailAddress;
        this.homeAddress = homeAddress;
    }

    public String getHomeAddress() {
        return homeAddress;
    }

    public void setHomeAddress(String homeAddress) {
        this.homeAddress = homeAddress;
    }
    
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public String getEmailAddress() {
        return emailAddress;
    }

    public void setEmailAddress(String emailAddress) {
        this.emailAddress = emailAddress;
    }
    
    public static void main(String[] args) {
        UserDetails user1 = new UserDetails("Alice", "123-456-7890", "alice@example.com", "123 Main St");
        UserDetails user2 = new UserDetails("Bob", "987-654-3210", "bob@example.com", "456 Elm St");

        System.out.println("User 1:");
        System.out.println("Name: " + user1.getName());
        System.out.println("Phone Number: " + user1.getPhoneNumber());
        System.out.println("Email Address: " + user1.getEmailAddress());
        System.out.println("Home Address: " + user1.getHomeAddress());

        System.out.println("\nUser 2:");
        System.out.println("Name: " + user2.getName());
        System.out.println("Phone Number: " + user2.getPhoneNumber());
        System.out.println("Email Address: " + user2.getEmailAddress());
        System.out.println("Home Address: " + user2.getHomeAddress());
    }
}