import subprocess, sys

def execute_script(script_path, input_data):
    try:
        # Start the subprocess to execute the script
        process = subprocess.Popen(
            ["python", script_path],  # Command to execute the script
            stdin=subprocess.PIPE,  # Open stdin for writing
            stdout=subprocess.PIPE,  # Open stdout for reading
            stderr=subprocess.PIPE,  # Open stderr for reading
            text=True  # Enable text mode
        )

        # Send input data and get output
        stdout, stderr = process.communicate(input=input_data)

        # Return the results
        return {
            "stdout": stdout,
            "stderr": stderr,
            "exit_code": process.returncode
        }

    except Exception as e:
        return {"error": str(e)}

arg = sys.argv[1]

# Open the file in read mode
with open(f"{arg}/input.txt", "r") as file:
    # Read all data from the file and store it in a string
    input_data = file.read()

# Open the file in read mode
with open(f"{arg}/output.txt", "r") as file:
    # Read all data from the file and store it in a string
    output_data = file.read()

script_path = f"{arg}/app.py"  # Path to the child script

result = execute_script(script_path, input_data)
output = result["stdout"]

print(output_data)
print(output)
    
print("Test Successful: ", output.strip()==output_data.strip())
