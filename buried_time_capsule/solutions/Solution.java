import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt(); // number of test cases
        
        for (int i = 0; i < t; i++) {
            int a = scanner.nextInt(); // steps forward
            int b = scanner.nextInt(); // steps backward
            int x = scanner.nextInt(); // target position
            
            System.out.println(findMinimumChecks(a, b, x));
        }
        scanner.close();
    }
    
    private static int findMinimumChecks(int a, int b, int x) {
        // If target is 0, we're already there
        if (x == 0) return 1;
        
        // If target is negative, convert problem to equivalent positive case
        if (x < 0) {
            x = -x;
            int temp = a;
            a = b;
            b = temp;
        }

        
        // Use BFS with bounded search space
        Queue<Long> queue = new LinkedList<>();
        Set<Long> visited = new HashSet<>();
        Map<Long, Integer> moves = new HashMap<>();
        
        queue.offer(0L);
        visited.add(0L);
        moves.put(0L, 0);
        
        while (!queue.isEmpty()) {
            long currentPos = queue.poll();
            int currentMoves = moves.get(currentPos);
            
            // Try moving forward
            long forwardPos = currentPos + a;
            if (forwardPos == x) {
                return currentMoves + 2;  // +1 for this move, +1 for initial check
            }
            
            if (!visited.contains(forwardPos) && forwardPos <= x + b && 
                Math.abs(forwardPos) <= 100000) {
                queue.offer(forwardPos);
                visited.add(forwardPos);
                moves.put(forwardPos, currentMoves + 1);
            }
            
            // Try moving backward
            long backwardPos = currentPos - b;
            if (backwardPos == x) {
                return currentMoves + 2;  // +1 for this move, +1 for initial check
            }
            
            if (!visited.contains(backwardPos) && backwardPos >= x - a && 
                Math.abs(backwardPos) <= 100000) {
                queue.offer(backwardPos);
                visited.add(backwardPos);
                moves.put(backwardPos, currentMoves + 1);
            }
        }
        
        return -1;
    }
    
    private static int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}