
from alive_progress import alive_bar
import time

# Define the total number of iterations
total_iterations = 200

# Create a progress bar using alive_bar
with alive_bar(total_iterations) as progress_bar:
    # Simulate a task that takes some time to complete
    for i in range(total_iterations):
        # Do some work
        time.sleep(0.1)        
        # Update the progress bar
        progress_bar()
