# 1. Opening and Closing a File
# Creates or opens a file in write mode, writes text, and closes it
f = open("example.txt", "w")
f.write("Hello, this is a text file!/n")
f.close()

# 2. Reading a File (Entire Content)
# Reads and prints the entire content of the file
f = open("example.txt", "r")
content = f.read()
print("reading entire file: ")
print(content)
f.close()

# 3. Reading Specific Number of Characters
# Reads first 5 characters from the file
f = open("example.txt", "r")
specific_content = f.read(5)
print("\nReading first 5 characters:")
print(specific_content)
f.close()

# 4. Reading a Line
# Reads one line at a time
f= open("example.txt", "r")
line = f.readline()
print("\nReading one line:")
print(line)
f.close()

# 5. Writing to a File
# Writes new content, overwriting existing content
f = open("example.txt", "w")
f.write("this overwrites the previous. \n")
f.close()

 # 6. Appending to a File
# Adds content to the end of the file without overwriting
f = open("example.txt", "a")
f.write("this is appended text.\n")
f.close()

# 7. Using 'with' Statement (No need to close explicitly)
# Writing using with statement
with open("example.txt", "w") as f:
    f.write("using with statement to write .\n")
    print("\n number of characters written: \n", f.write("you are awesome\n"))

# Reading using with statement
with open("example.txt", "r") as f:
    print("\nReading with 'with statement:")
    print(f.read())

# 8. Copying Content from One File to Another
# Create a source file
with open("source.txt", "w") as f:
    f.write("content to be copied\n")

# Copy content to destination file
with open("source.txt", "r") as f:
    copy_content = f.read()

with open("destination.txt", "w") as f:
    f.write(copy_content)

# Read and verify copied content
with open("destination.txt", "r") as f:
    print("\ncontent of destination file after copying")
    print(f.read())

# 9. Moving a File
import shutil
with open("file_to_move.txt", "w") as f:
    f.write("this file will be moved.\n")

# Verify moved file
# with open("moved_file.txt", "r") as f:
    print("content of moved file: ")
    # print(f.read())

# 10. Removing a File
import os
# Create a file to delete
with open("file_to_delete.txt", "w") as f:
    f.write("this file will be deleted.\n")

# Delete the file
os.remove("file_to_delete.txt")
print("\nFile 'file_to_delete.txt' has been deleted.")

# 11. Renaming a File
# Create a file to rename
with open("old_name.txt", "w") as f:
    f.write("this file will be renamed.\n")

# os.remove("old_name.txt", "new_name.txt")
# print("\n file renamed to 'new_name.txt'")

# verify renamed file
with open("new_name.txt", "r") as f:
    print("content fo renamed")
    print(f.read())
