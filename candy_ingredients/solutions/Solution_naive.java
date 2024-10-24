import java.util.*;

public class Solution {
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
            int curCount = 0;
           for (int i = 97; i < 97 + 26; i++) {
               final int c = i;
               if(candy.chars().filter(ch -> ch ==(char)(c)).count() > 0) {
                    curCount += 1;
               }
           }
           if (curCount > maxUniqueIngredients) {
                maxUniqueIngredients = curCount;
               candyWithMostIngredients = candy;
           }
        }
        
        // Output the candy with the most unique ingredients and the count
        System.out.println(candyWithMostIngredients + " " + maxUniqueIngredients);
        
        sc.close();
    }
}
