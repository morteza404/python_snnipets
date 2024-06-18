from tasks import add

result = add.delay(4, 6)  # Call the task asynchronously

# Do other work while the task is being processed...

print(result.get())  # Get the result of the task (blocking)
