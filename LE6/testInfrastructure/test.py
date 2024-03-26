import subprocess
import os

def run_cpp_file():
    cpp_filename = 'lru_test.cpp'
    compile_process = subprocess.run(["g++", "-std=c++17", cpp_filename, "-o", "temp_executable"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check for compilation errors
    if compile_process.returncode != 0:
        print("Compilation error:")
        print(compile_process.stderr)
        return

    # Run the compiled executable
    run_process = subprocess.run(["./temp_executable"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Print the output and error
    print(run_process.stdout)

    if(run_process.stderr):
        print("Error:")
        print(run_process.stderr)
    
    try:
        os.remove("./temp_executable")
    except FileNotFoundError:
        print("Compilation error")

run_cpp_file()
