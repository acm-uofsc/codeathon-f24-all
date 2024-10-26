import java.util.*;
import java.io.*;

public class ApprovalHierarchy {
    static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

    private static String readLine() throws IOException {
        return reader.readLine().trim();
    }

    private static int[] readNumbers() throws IOException {
        return Arrays.stream(readLine().split("\\s+"))
                    .mapToInt(Integer::parseInt)
                    .toArray();
    }

    private static int runCase() throws IOException {
        // Read initial counts
        int[] counts = readNumbers();
        int needsApprovalCount = counts[0];
        int totalMembers = counts[1];
        assert needsApprovalCount <= totalMembers;

        // Read all names
        String[] allNames = readLine().split("\\s+");
        Set<String> uniqueNames = new HashSet<>(Arrays.asList(allNames));
        assert uniqueNames.size() == allNames.length;

        // Initialize data structures
        Map<String, Integer> personToRemainingApprovals = new HashMap<>();
        Map<String, List<String>> personToApproverNames = new HashMap<>();
        Map<String, List<String>> higherPowerToLower = new HashMap<>();

        // Process each person needing approval
        for (int i = 0; i < needsApprovalCount; i++) {
            String[] parts = readLine().split("\\s+");
            String person = parts[0];
            int minNeeded = Integer.parseInt(parts[1]);
            int hiAllowed = Integer.parseInt(parts[2]);

            assert minNeeded <= hiAllowed : minNeeded + ", " + hiAllowed;
            personToRemainingApprovals.put(person, minNeeded);

            // Read approver positions and convert to names
            int[] approverPositions = readNumbers();
            List<String> approverNames = new ArrayList<>();
            for (int pos : approverPositions) {
                approverNames.add(allNames[pos]);
            }

            assert !approverNames.contains(person) : person;
            personToApproverNames.put(person, approverNames);

            // Build reverse mapping
            for (String approver : approverNames) {
                higherPowerToLower.computeIfAbsent(approver, k -> new ArrayList<>())
                                .add(person);
            }
        }

        // Initialize fringe with names that don't need approval
        Deque<String> fringe = new ArrayDeque<>();
        for (String name : allNames) {
            if (personToRemainingApprovals.getOrDefault(name, 0) == 0) {
                fringe.add(name);
            }
        }

        Set<String> seen = new HashSet<>();
        int ret = 0;

        while (!fringe.isEmpty()) {
            String curName = fringe.poll();
            if (seen.contains(curName)) {
                continue;
            }

            seen.add(curName);

            if (personToRemainingApprovals.getOrDefault(curName, 0) <= 0) {
                ret++;
                List<String> lowerDownPeople = higherPowerToLower.getOrDefault(curName, Collections.emptyList());
                for (String lowerDownPerson : lowerDownPeople) {
                    int approvals = personToRemainingApprovals.get(lowerDownPerson) - 1;
                    personToRemainingApprovals.put(lowerDownPerson, approvals);
                    if (approvals <= 0) {
                        fringe.add(lowerDownPerson);
                    }
                }
            }
        }

        assert ret <= totalMembers;
        return ret;
    }

    public static void main(String[] args) throws IOException {
        int cases = Integer.parseInt(readLine());
        for (int i = 0; i < cases; i++) {
            System.out.println(runCase());
        }
    }
}