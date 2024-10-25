import java.io.*;
import java.util.*;
//made using claude
public class Solution {
    static Map<Character, Character> operatorMap = new HashMap<>();
    static String operatorOrder;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // Read operator order
        operatorOrder = br.readLine();
        
        // Build operator map
        for (int i = 0; i < operatorOrder.length(); i++) {
            String[] op = br.readLine().split(" ");
            char letter = op[0].charAt(0);
            char operator = op[1].charAt(0);
            operatorMap.put(letter, operator);
        }
        
        // Read number of equations
        int n = Integer.parseInt(br.readLine());
        
        // Process each equation
        for (int i = 0; i < n; i++) {
            String equation = br.readLine();
            long result = evaluateExpression(equation);
            System.out.println(result);
        }
    }
    
    private static long evaluateExpression(String equation) {
        List<String> tokens = tokenize(equation);
        return evaluate(tokens);
    }
    
    private static List<String> tokenize(String equation) {
        List<String> tokens = new ArrayList<>();
        StringBuilder num = new StringBuilder();
        
        for (char c : equation.toCharArray()) {
            if (Character.isDigit(c)) {
                num.append(c);
            } else if (c == ' ') {
                if (num.length() > 0) {
                    tokens.add(num.toString());
                    num = new StringBuilder();
                }
            } else {
                if (num.length() > 0) {
                    tokens.add(num.toString());
                    num = new StringBuilder();
                }
                tokens.add(String.valueOf(c));
            }
        }
        if (num.length() > 0) {
            tokens.add(num.toString());
        }
        return tokens;
    }
    
    private static long evaluate(List<String> tokens) {
        // Handle parentheses first
        while (tokens.contains("(")) {
            int open = -1;
            int close = -1;
            int parenCount = 0;
            
            for (int i = 0; i < tokens.size(); i++) {
                if (tokens.get(i).equals("(")) {
                    if (parenCount == 0) {
                        open = i;
                    }
                    parenCount++;
                } else if (tokens.get(i).equals(")")) {
                    parenCount--;
                    if (parenCount == 0) {
                        close = i;
                        List<String> subExpr = new ArrayList<>(tokens.subList(open + 1, close));
                        long result = evaluate(subExpr);
                        
                        // Replace parentheses and contents with result
                        for (int j = 0; j < close - open + 1; j++) {
                            tokens.remove(open);
                        }
                        tokens.add(open, String.valueOf(result));
                        break;
                    }
                }
            }
        }
        
        // Process operators in order of precedence
        for (char letter : operatorOrder.toCharArray()) {
            while (true) {
                int opIndex = -1;
                for (int i = 0; i < tokens.size(); i++) {
                    if (tokens.get(i).length() == 1 && tokens.get(i).charAt(0) == letter) {
                        opIndex = i;
                        break;
                    }
                }
                
                if (opIndex == -1) break;
                
                long left = Long.parseLong(tokens.get(opIndex - 1));
                long right = Long.parseLong(tokens.get(opIndex + 1));
                long result = applyOperator(left, right, operatorMap.get(letter));
                
                tokens.remove(opIndex - 1);
                tokens.remove(opIndex - 1);
                tokens.remove(opIndex - 1);
                tokens.add(opIndex - 1, String.valueOf(result));
            }
        }
        
        return Long.parseLong(tokens.get(0));
    }
    
    private static long applyOperator(long a, long b, char op) {
        switch (op) {
            case '+': return a + b;
            case '-': return a - b;
            case '*': return a * b;
            default: throw new IllegalArgumentException("Unknown operator: " + op);
        }
    }
}