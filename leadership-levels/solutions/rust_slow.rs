use std::collections::{HashMap, HashSet};
use std::io::{self, BufRead};

fn run_case() -> io::Result<usize> {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();
    
    // Read needs_approval_count and total_members
    let first_line = lines.next().unwrap()?;
    let mut nums = first_line.split_whitespace()
        .map(|x| x.parse::<usize>().unwrap());
    let needs_approval_count = nums.next().unwrap();
    let total_members = nums.next().unwrap();
    
    // Read all names
    let all_names: Vec<String> = lines.next().unwrap()?
        .split_whitespace()
        .map(|s| s.to_string())
        .collect();
    
    // Initialize data structures for people who need approval
    let mut person_to_min_count_needed: HashMap<String, usize> = HashMap::new();
    let mut person_to_approver_names: HashMap<String, Vec<String>> = HashMap::new();
    
    // Process each person needing approval
    for _ in 0..needs_approval_count {
        let person_line = lines.next().unwrap()?;
        let person_info: Vec<&str> = person_line.split_whitespace().collect();
        let person = person_info[0].to_string();
        let min_needed = person_info[1].parse::<usize>().unwrap();
        let _hi_allowed = person_info[2].parse::<usize>().unwrap();
        
        person_to_min_count_needed.insert(person.clone(), min_needed);
        
        // Read and process approver positions
        let approver_line = lines.next().unwrap()?;
        if !approver_line.trim().is_empty() {
            let approver_names: Vec<String> = approver_line
                .split_whitespace()
                .map(|pos| all_names[pos.parse::<usize>().unwrap()].clone())
                .collect();
            person_to_approver_names.insert(person, approver_names);
        } else {
            person_to_approver_names.insert(person, Vec::new());
        }
    }
    
    // Process approvals
    let mut given_approval = HashSet::new();
    
    // Add all people who don't need approval initially
    for name in &all_names {
        if !person_to_min_count_needed.contains_key(name) {
            given_approval.insert(name.clone());
        }
    }
    
    let mut changed = true;
    while changed {
        changed = false;
        for name in &all_names {
            if given_approval.contains(name) {
                continue;
            }
            
            let min_needed = match person_to_min_count_needed.get(name) {
                Some(&min) => min,
                None => continue,
            };
            
            let approvals = person_to_approver_names
                .get(name)
                .map(|approvers| {
                    approvers.iter()
                        .filter(|approver| given_approval.contains(*approver))
                        .count()
                })
                .unwrap_or(0);
            
            if approvals >= min_needed {
                given_approval.insert(name.clone());
                changed = true;
            }
        }
    }
    
    Ok(given_approval.len())
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let cases = stdin.lock().lines().next().unwrap()?.parse::<i32>().unwrap();
    
    for _ in 0..cases {
        let result = run_case()?;
        println!("{}", result);
    }
    
    Ok(())
}