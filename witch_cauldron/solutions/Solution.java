import java.io.*;
import java.util.*;

public class Solution {
    static class Ingredient {
        int worry;
        int magic;
        
        Ingredient(int worry, int magic) {
            this.worry = worry;
            this.magic = magic;
        }
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // Read ingredients
        int n = sc.nextInt();
        List<Ingredient> ingredients = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int worry = sc.nextInt();
            int magic = sc.nextInt();
            ingredients.add(new Ingredient(worry, magic));
        }
        
        // Pre-calculate all possible states
        // dp[i][w] represents max magic for first i ingredients at worry level w
        int maxWorry = 2000;  // given constraint
        int[][] dp = new int[n + 1][maxWorry + 1];
        
        // Initialize with -1 to distinguish between "not possible" and "possible with 0 magic"
        for (int[] row : dp) {
            Arrays.fill(row, -1);
        }
        dp[0][0] = 0;  // base case: empty selection has 0 magic and 0 worry
        
        // Calculate full DP table for all ingredients
        for (int i = 0; i < n; i++) {
            Ingredient curr = ingredients.get(i);
            
            for (int w = 0; w <= maxWorry; w++) {
                if (dp[i][w] != -1) {
                    // Don't take current ingredient
                    dp[i + 1][w] = Math.max(dp[i + 1][w], dp[i][w]);
                    
                    // Take current ingredient if possible
                    if (w + curr.worry <= maxWorry) {
                        dp[i + 1][w + curr.worry] = Math.max(
                            dp[i + 1][w + curr.worry], 
                            dp[i][w] + curr.magic
                        );
                    }
                }
            }
            
            // Optional optimization: After calculating each row, update best values
            // This ensures each position holds the best value possible using up to i ingredients
            for (int w = 0; w <= maxWorry; w++) {
                if (w > 0 && dp[i + 1][w - 1] > dp[i + 1][w]) {
                    dp[i + 1][w] = dp[i + 1][w - 1];
                }
            }
        }
        
        // Process queries efficiently using pre-calculated table
        int q = sc.nextInt();
        while (q-- > 0) {
            int queryWorry = sc.nextInt();
            int k = sc.nextInt();  // number of first ingredients to consider
            System.out.println(dp[k][queryWorry]);
        }
        
        // System.out.print(output);  // Print all results at once
    }
}