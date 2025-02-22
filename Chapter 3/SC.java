public class SC {
    // Method to compress a string using the counts of repeated characters
    public static String cS(String s) {
        // If the string is null or empty, return it as is
        if (s == null || s.isEmpty()) {
            return s;
        }
        
        // StringBuilder to build the compressed string
        StringBuilder sb = new StringBuilder();
        // Counter for the occurrences of each character
        int c = 1;
        
        // Loop through the string
        for (int i = 0; i < s.length(); i++) {
            // If the current character is the same as the next one, increment the counter
            if (i + 1 < s.length() && s.charAt(i) == s.charAt(i + 1)) {
                c++;
            } else {
                // Otherwise, append the character and its count to the StringBuilder
                sb.append(s.charAt(i)).append(c);
                // Reset the counter
                c = 1;
            }
        }
        
        // Return the compressed string if it's shorter than the original, otherwise return the original string
        return sb.length() < s.length() ? sb.toString() : s;
    }

    public static void main(String[] a) {
        String x = "aaabbcddddee";
        System.out.println("Original: " + x);
        System.out.println("Compressed: " + cS(x));
    }
}