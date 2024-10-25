import os
import shutil
import subprocess

# Remove existing input and output directories if they exist
if os.path.exists('input'):
    shutil.rmtree('input')
if os.path.exists('output'):
    shutil.rmtree('output')

# Create new input and output directories
os.makedirs('input', exist_ok=True)
os.makedirs('output', exist_ok=True)

# Copy over samples
if os.path.exists('samples/input'):
    shutil.copytree('samples/input', 'input', dirs_exist_ok=True)
if os.path.exists('samples/output'):
    shutil.copytree('samples/output', 'output', dirs_exist_ok=True)


# Generate input/output files for range 2 to 50
for i in range(0, 41):
    print(i)
    input_file = f'input/input{i}.txt'
    output_file = f'output/output{i}.txt'

    try:
        # Run the command and check if it fails
        worked = subprocess.run(f'echo {i} | python3 ./mkin.py > {input_file}', 
                                shell=True, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        # Print the error and exit if the command fails
        print(f"Error generating input for case {i}: {e.stderr}")
        exit()

    # Run the solution using the generated input
    try:
        worked = subprocess.run(f'python3 ./solutions/sol.py < {input_file} > {output_file}', 
                                shell=True, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        # Print the error and exit if the command fails
        print(f"Error running solution for case {i}: {e.stderr}")
        exit()

    # # #check against other solutions
    # try:
    #     temp_file = "temp.txt"
    #     worked = subprocess.run(f'python3 ./solutions/gptv2.py < {input_file} > {temp_file}', 
    #                             shell=True, check=True, capture_output=True, text=True)
    #     worked = subprocess.run(f'diff -u {output_file} {temp_file}', 
    #                             shell=True, check=True, capture_output=True, text=True)
    #     if worked.stdout.strip():
    #         print("diff was different")
    #         raise ValueError("diff was different")
    # except subprocess.CalledProcessError as e:
    #     # Print the error and exit if the command fails
    #     print(f"Error running solution for case {i}: {e.stdout} {e.stderr}")
        # exit()
    


# Remove existing cases.zip if it exists
if os.path.exists('cases.zip'):
    os.remove('cases.zip')

os.system("zip -r cases input output")
# os.system(f"rm {temp_file}")