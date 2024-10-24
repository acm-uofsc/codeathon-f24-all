import java.util.*;

public class CandyIngredients {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // Reading input
        int n = sc.nextInt(); // number of candy bars
        sc.nextLine(); // consume the remaining newline
        String[] candies = sc.nextLine().split(" "); // space-separated candy bars
        
        String candyWithMostIngredients = "";
        int maxUniqueIngredients = 0;
        
        // Iterate through each candy
        for (String candy : candies) {
            // Use a set to find unique ingredients
            Set<Character> uniqueIngredients = new HashSet<>();
            for (char c : candy.toCharArray()) {
                uniqueIngredients.add(c);
            }
            
            // Check if this candy has more unique ingredients than the current maximum
            if (uniqueIngredients.size() > maxUniqueIngredients) {
                maxUniqueIngredients = uniqueIngredients.size();
                candyWithMostIngredients = candy;
            }
        }
        
        // Output the candy with the most unique ingredients and the count
        System.out.println(candyWithMostIngredients + " " + maxUniqueIngredients);
        
        sc.close();
    }
}
