import subprocess
import time

def check_code_quality():
    print("Running pylint for code quality...")
    result = subprocess.run(['pylint', 'server.py', 'client.py'], capture_output=True, text=True)
    
    # Output pylint report
    print(result.stdout)

    # Extract pylint score from the report (out of 10)
    for line in result.stdout.splitlines():
        if line.startswith('Your code has been rated at'):
            print(f"Pylint score: {line.split()[6]}")
            break

def check_test_coverage():
    print("\nRunning tests for code coverage...")
    subprocess.run(['coverage', 'run', '-m', 'unittest', 'discover'], check=True)
    result = subprocess.run(['coverage', 'report', '-m'], capture_output=True, text=True)
    
    # Output coverage report
    print(result.stdout)

if __name__ == '__main__':
    check_code_quality()
    time.sleep(10)
    check_test_coverage()
