use std::collections::{HashMap, HashSet, VecDeque};
use std::io::{self, BufRead};

fn read_line() -> String {
    let mut line = String::new();
    io::stdin().lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn read_numbers() -> Vec<i32> {
    read_line()
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect()
}

fn run_case() -> i32 {
    // Read initial counts
    let counts: Vec<i32> = read_numbers();
    let (needs_approval_count, total_members) = (counts[0], counts[1]);
    assert!(needs_approval_count <= total_members);

    // Read all names
    let all_names: Vec<String> = read_line()
        .split_whitespace()
        .map(String::from)
        .collect();
    
    let unique_names: HashSet<_> = all_names.iter().collect();
    assert_eq!(unique_names.len(), all_names.len());

    // Initialize data structures
    let mut person_to_remaining_approvals: HashMap<String, i32> = HashMap::new();
    let mut person_to_approver_names: HashMap<String, Vec<String>> = HashMap::new();
    let mut higher_power_to_lower: HashMap<String, Vec<String>> = HashMap::new();

    // Process each person needing approval
    for _ in 0..needs_approval_count {
        let line = read_line();
        let parts: Vec<&str> = line.split_whitespace().collect();
        let (person, min_needed, hi_allowed) = (
            parts[0].to_string(),
            parts[1].parse::<i32>().unwrap(),
            parts[2].parse::<i32>().unwrap()
        );
        
        assert!(min_needed <= hi_allowed);
        person_to_remaining_approvals.insert(person.clone(), min_needed);

        // Read approver positions and convert to names
        let approver_positions: Vec<usize> = read_numbers()
            .into_iter()
            .map(|x| x as usize)
            .collect();
            
        let approver_names: Vec<String> = approver_positions
            .iter()
            .map(|&pos| all_names[pos].clone())
            .collect();

        assert!(!approver_names.contains(&person));
        
        person_to_approver_names.insert(person.clone(), approver_names.clone());
        
        // Build reverse mapping
        for approver in approver_names {
            higher_power_to_lower
                .entry(approver)
                .or_insert_with(Vec::new)
                .push(person.clone());
        }
    }

    // Initialize fringe with names that don't need approval
    let mut fringe: VecDeque<String> = all_names
        .into_iter()
        .filter(|name| !person_to_remaining_approvals.contains_key(name) || person_to_remaining_approvals[name] == 0)
        .collect();

    let mut seen: HashSet<String> = HashSet::new();
    let mut ret = 0;

    while let Some(cur_name) = fringe.pop_front() {
        if seen.contains(&cur_name) {
            continue;
        }
        
        seen.insert(cur_name.clone());
        
        if person_to_remaining_approvals.get(&cur_name).unwrap_or(&0) <= &0 {
            ret += 1;
            
            if let Some(lower_down_people) = higher_power_to_lower.get(&cur_name) {
                for lower_down_person in lower_down_people {
                    if let Some(approvals) = person_to_remaining_approvals.get_mut(lower_down_person) {
                        *approvals -= 1;
                        if *approvals <= 0 {
                            fringe.push_back(lower_down_person.clone());
                        }
                    }
                }
            }
        }
    }

    assert!(ret <= total_members);
    ret
}

fn main() {
    let cases: i32 = read_line().parse().unwrap();
    for _ in 0..cases {
        println!("{}", run_case());
    }
}