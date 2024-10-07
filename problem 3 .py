import os

# Specify the directory path (use '.' for the current directory)
directory = '/New folder'

# List the contents of the directory
contents = os.listdir(directory)

# Print the contents
for item in contents:
    print(item)
