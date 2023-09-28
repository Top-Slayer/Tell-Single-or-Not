import subprocess

# Run the first Python file in the background
process1 = subprocess.Popen(['python', 'Detect_people.py'])

# Run the second Python file in the background
process2 = subprocess.Popen(['python', 'Playsound.py'])

# Wait for both processes to complete
process1.wait()
process2.wait()