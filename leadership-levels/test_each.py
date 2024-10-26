import subprocess
import os

# Generate input/output files for range 2 to 50
for i in range(0, 41):
    print(i)
    input_file = f'input/input{i}.txt'
    output_file = f'output/output{i}.txt'

    # Run the solution using the generated input
    worked = os.system(f'python ./solutions/sol.py < {input_file} > temp2.txt') 
    # try:
    #                             shell=True, check=True, capture_output=True, text=True)
    # except subprocess.CalledProcessError as e:
    #     # Print the error and exit if the command fails
    #     print(f"Error running solution for case {i}: {e.stderr}")
    #     exit()