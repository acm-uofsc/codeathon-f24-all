import java.util.*;

public class Solution {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();  // Number of test cases
        
        for (int i = 0; i < t; i++) {
            int a = scanner.nextInt();  // Forward steps
            int b = scanner.nextInt();  // Backward steps
            int x = scanner.nextInt();  // Target distance

            System.out.println(minPhoneChecks(a, b, x));
        }
    }

    public static int minPhoneChecks(int a, int b, int x) {
        // BFS uses a queue to track positions and the number of moves to reach them
        Queue<int[]> queue = new LinkedList<>();
        Set<Integer> visited = new HashSet<>();  // To avoid revisiting the same position
        
        queue.offer(new int[]{0, 1});  // Start at position 0 with 0 moves
        visited.add(0);

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int position = current[0];
            int moves = current[1];

            // If we reached the target, return the number of moves (phone checks)
            if (position == x) {
                return moves;
            }

            // Move forward by 'a' steps
            int forward = position + a;
            if (!visited.contains(forward) && forward <= x + b) { // Limit how far we can move forward
                visited.add(forward);
                queue.offer(new int[]{forward, moves + 1});
            }

            // Move backward by 'b' steps
            int backward = position - b;
            if (backward >= 0 && !visited.contains(backward)) {  // Only consider valid positions (>= 0)
                visited.add(backward);
                queue.offer(new int[]{backward, moves + 1});
            }
        }

        // If we exhausted all possibilities and never reached `x`, return -1 (impossible)
        return -1;
    }
}
