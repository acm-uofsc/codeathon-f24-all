use std::io::{self, BufRead, Write};

struct Ingredient {
    worry: i32,
    magic: i32,
}

fn main() {
    let stdin = io::stdin();
    let stdout = io::stdout();
    let mut lines = stdin.lock().lines();
    let mut output = stdout.lock();
    
    // Read number of ingredients
    let n: usize = lines.next().unwrap().unwrap()
        .trim().parse().unwrap();
    
    // Read ingredients
    let mut ingredients = Vec::with_capacity(n);
    for _ in 0..n {
        let line = lines.next().unwrap().unwrap();
        let nums: Vec<i32> = line.split_whitespace()
            .map(|x| x.parse().unwrap())
            .collect();
            
        ingredients.push(Ingredient {
            worry: nums[0],
            magic: nums[1],
        });
    }
    
    // Pre-calculate dp table for all ingredients up to max worry level
    const MAX_WORRY: usize = 2000;
    
    // Read and process queries efficiently
    let q: i32 = lines.next().unwrap().unwrap()
        .trim().parse().unwrap();
        
    // Use a string buffer for output
    let mut result = String::with_capacity(q as usize * 10);
    
    // Process each query
    for _ in 0..q {
        let line = lines.next().unwrap().unwrap();
        let nums: Vec<i32> = line.split_whitespace()
            .map(|x| x.parse().unwrap())
            .collect();
        
        let query_worry = nums[0] as usize;
        let dp = calculate_all_states(&ingredients, query_worry);
        let k = nums[1] as usize;
        
        // Simply look up the pre-calculated value
        result.push_str(&dp[k][query_worry].to_string());
        result.push('\n');
    }
    
    // Write all output at once
    output.write_all(result.as_bytes()).unwrap();
}

fn calculate_all_states(ingredients: &[Ingredient], max_worry: usize) -> Vec<Vec<i32>> {
    let n = ingredients.len();
    let mut dp = vec![vec![-1; max_worry + 1]; n + 1];
    dp[0][0] = 0;  // base case: empty selection has 0 magic and 0 worry
    
    // Calculate full DP table for all ingredients
    for i in 0..n {
        let curr = &ingredients[i];
        
        for w in 0..=max_worry {
            if dp[i][w] != -1 {
                // Don't take current ingredient
                dp[i + 1][w] = dp[i + 1][w].max(dp[i][w]);
                
                // Take current ingredient if possible
                if w + curr.worry as usize <= max_worry {
                    dp[i + 1][w + curr.worry as usize] = dp[i + 1][w + curr.worry as usize].max(
                        dp[i][w] + curr.magic
                    );
                }
            }
        }
        
        // Optimization: Ensure each position contains the best possible value
        // by propagating better values from lower worry levels
        for w in 1..=max_worry {
            if dp[i + 1][w - 1] > dp[i + 1][w] {
                dp[i + 1][w] = dp[i + 1][w - 1];
            }
        }
    }
    
    dp
}