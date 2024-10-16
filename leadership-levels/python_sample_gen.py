import os
import subprocess

# Create the directories if they do not exist
os.makedirs('samples/input', exist_ok=True)
os.makedirs('samples/output', exist_ok=True)

for i in range(0, 1):  # Loop from 0 to 0
    input_file = f'samples/input/input{i}.txt'
    output_file = f'samples/output/output{i}.txt'
    
    # Run mkin.py and save the output to the input file
    with open(input_file, 'w') as infile:
        subprocess.run(f'echo {i} | python3 ./mkin.py', shell=True, check=True, stdout=infile)
    
    # Run sol.py with the generated input and save the output to the output file
    with open(output_file, 'w') as outfile:
        subprocess.run(f'python3 solutions/sol.py < {input_file}', shell=True, check=True, stdout=outfile)

    print(f"Processed case {i}: {input_file} -> {output_file}")
