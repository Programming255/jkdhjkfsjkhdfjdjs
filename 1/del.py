import os

# list of files to be deleted
files_to_delete = ['liveip.txt', 'reversed.txt']

# loop through the list of files
for file in files_to_delete:
    try:
        # attempt to delete the file
        os.remove(file)
        print(f"{file} deleted successfully")
    except FileNotFoundError:
        # print error message if file not found
        print(f"Error: {file} not found")
