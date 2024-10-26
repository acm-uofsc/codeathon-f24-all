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
        
        // Handle negative target
        if (x < 0) {
            x = -x;
            int temp = a;
            a = b;
            b = temp;
        }
        
        // Check if solution is possible using GCD
        int gcd = gcd(a, b);
        if (x % gcd != 0) {
            return -1;
        }
        
        // Special case: when forward and backward steps are equal
        if (a == b) {
            if (x % a == 0) {
                return x / a + 1;  // +1 for initial check
            }
            return -1;
        }
        
        // For small numbers, use BFS
        if (x <= 20000) {
            return bfs(a, b, x);
        }
        
        // For larger numbers, use mathematical solution
        // Calculate minimum positive solution using extended Euclidean algorithm
        int[] bezout = extendedGCD(a, b);
        int m = bezout[0];
        int n = bezout[1];
        
        // Find smallest positive values for m and n that reach x
        long k = (long)x / gcd;
        long m1 = k * m;
        long n1 = k * n;
        
        // Adjust m1 and n1 to be minimal positive values
        long d = Math.min(m1 / (b/gcd), -n1 / (a/gcd));
        m1 = m1 - d * (b/gcd);
        n1 = n1 + d * (a/gcd);
        
        while (m1 < 0 || n1 < 0) {
            if (m1 < 0) {
                m1 += b/gcd;
                n1 -= a/gcd;
            }
            if (n1 < 0) {
                m1 -= b/gcd;
                n1 += a/gcd;
            }
        }
        
        return (int)(m1 + n1 + 1); // +1 for initial check
    }
    
    private static int bfs(int a, int b, int x) {
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
                return currentMoves + 2;
            }
            
            if (!visited.contains(forwardPos) && forwardPos <= x + b) {
                queue.offer(forwardPos);
                visited.add(forwardPos);
                moves.put(forwardPos, currentMoves + 1);
            }
            
            // Try moving backward
            long backwardPos = currentPos - b;
            if (backwardPos == x) {
                return currentMoves + 2;
            }
            
            if (!visited.contains(backwardPos) && backwardPos >= x - a) {
                queue.offer(backwardPos);
                visited.add(backwardPos);
                moves.put(backwardPos, currentMoves + 1);
            }
        }
        
        return -1;
    }
    
    private static int[] extendedGCD(int a, int b) {
        if (b == 0) {
            return new int[] {1, 0};
        }
        
        int[] vals = extendedGCD(b, a % b);
        int m = vals[1];
        int n = vals[0] - vals[1] * (a / b);
        
        return new int[] {m, n};
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