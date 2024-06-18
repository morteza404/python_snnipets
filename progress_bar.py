import sys
from time import sleep


def update_progress(progress, total):
    """
    Prints a progress bar to the console.

    Args:
      progress: The current progress (number of completed items).
      total: The total number of items.
    """
    progress_bar = "=" * int(progress / total * 50)
    remaining = " " * (50 - len(progress_bar))
    sys.stdout.write(f"\r[{progress_bar}{remaining}] {100 * progress/total:.2f}%")
    sys.stdout.flush()  # Force update the console output


# Example usage
total_items = 100
for i in range(total_items):
    # Some task
    update_progress(i + 1, total_items)
    sleep(0.2)

print("\nDone!")
