import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // Reading input
        int n = sc.nextInt(); // number of tiles
        int s = sc.nextInt(); // number of seconds (moves)
        int[] tiles = new int[n];
        
        for (int i = 0; i < n; i++) {
            tiles[i] = sc.nextInt();
        }
        
        // Jerry starts at the first tile (index 0)
        int currentPosition = 0;
        
        // Simulate Jerry's moves for 's' seconds
        for (int i = 0; i < s; i++) {
            // Move right by 1 tile
            currentPosition = (currentPosition + 1) % n;
            
            // Check if Jerry falls (the tile is '0')
            if (tiles[currentPosition] == 0) {
                tiles[currentPosition] = 5;  // Fill the fallen tile with '5'
                currentPosition = 0;         // Jerry respawns at the beginning
            }
        }
        
        // Output the tile Jerry ends up on after 's' moves
        System.out.println(tiles[currentPosition]);
        
        sc.close();
    }
}
