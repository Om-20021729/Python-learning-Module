import os

# Get the directory path from the user
directory_path = '/'

    # List all entries in the specified directory
contents = os.listdir(directory_path)
    
print(f"Contents of the directory '{directory_path}':")
for item in contents:
    print(item)