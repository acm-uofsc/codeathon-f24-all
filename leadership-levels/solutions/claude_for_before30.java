import java.io.*;
import java.util.*;

public class Solution {
    static class Person {
        String name;
        int minApprovals;
        List<Integer> canApproveFrom;
        
        Person(String name, int minApprovals, List<Integer> canApproveFrom) {
            this.name = name;
            this.minApprovals = minApprovals;
            this.canApproveFrom = canApproveFrom;
        }
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int testCases = Integer.parseInt(reader.readLine().trim());
        
        for (int t = 0; t < testCases; t++) {
            // Read N and M
            String[] nm = reader.readLine().trim().split(" ");
            int n = Integer.parseInt(nm[0]); // number of people requiring approval
            int m = Integer.parseInt(nm[1]); // total number of people
            
            // Read names
            String[] names = reader.readLine().trim().split(" ");
            
            // Create person objects
            Map<String, Person> peopleMap = new HashMap<>();
            Set<String> allNames = new HashSet<>(Arrays.asList(names));
            
            // Read N descriptions
            for (int i = 0; i < n; i++) {
                String[] line = reader.readLine().trim().split(" ");
                String name = line[0];
                int minApprovals = Integer.parseInt(line[1]);
                int totalPossibleApprovals = Integer.parseInt(line[2]);
                
                List<Integer> approvers = new ArrayList<>();
                if (totalPossibleApprovals > 0) {
                    String[] approverIndices = reader.readLine().trim().split(" ");
                    for (String idx : approverIndices) {
                        approvers.add(Integer.parseInt(idx));
                    }
                } else {
                    reader.readLine(); // read empty line
                }
                
                peopleMap.put(name, new Person(name, minApprovals, approvers));
            }
            
            System.out.println(calculateApprovals(peopleMap, names));
        }
    }
    
    private static int calculateApprovals(Map<String, Person> peopleMap, String[] allNames) {
        Set<String> canApprove = new HashSet<>();
        
        // Initially add all people who aren't in peopleMap (they can always approve)
        for (String name : allNames) {
            if (!peopleMap.containsKey(name)) {
                canApprove.add(name);
            }
        }
        
        boolean changed;
        do {
            changed = false;
            
            // For each person who needs approval
            for (Map.Entry<String, Person> entry : peopleMap.entrySet()) {
                if (canApprove.contains(entry.getKey())) {
                    continue;
                }
                
                Person person = entry.getValue();
                int approvalCount = 0;
                
                // Count approvals they can get
                for (int approverIdx : person.canApproveFrom) {
                    String approverName = allNames[approverIdx];
                    if (canApprove.contains(approverName)) {
                        approvalCount++;
                    }
                }
                
                // If they have enough approvals, mark them as approved
                if (approvalCount >= person.minApprovals) {
                    canApprove.add(person.name);
                    changed = true;
                }
            }
        } while (changed);
        
        return canApprove.size();
    }
}