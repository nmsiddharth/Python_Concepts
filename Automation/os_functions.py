import os

# Define a list of path components
full_path = ['folder1', 'folder2', 'file1.png']

# Join the path components
joined_path = os.path.join(*full_path)
print("Joined Path:", joined_path)

# Get and print the current working directory
current_directory = os.getcwd()
print("Current Working Directory:", current_directory)

# Change directory to C:\
os.chdir('C:\\')  # This will change the current working directory to C:\

# Checking current working directory
current_directory = os.getcwd()
print("Current Working Directory:", current_directory)

# Print the absolute path of 'Automating_Linux_Tasks'
absolute_path = os.path.abspath('Automating_Linux_Tasks')
print("Absolute Path of 'Automating_Linux_Tasks':", absolute_path)

# Check if 'Automating_Linux_Tasks' is an absolute path
is_absolute = os.path.isabs('/')
print("Is 'Automating_Linux_Tasks' an absolute path?", is_absolute)

# Print Relative path
relative_path = os.path.relpath('/', 'D:\\SIDDU\\Technical\\Python')
print(relative_path)

# Prints Directory path
dir_path = os.path.dirname(joined_path)
print(dir_path)

# Prints Last Folder/file name
last_path = os.path.basename(joined_path)
print(last_path)

# Prints True/False if Path exists in system or not
exists_or_not = os.path.exists(joined_path)
print(exists_or_not)

# Creates new Folder
print(os.makedirs('D:\\SIDDU\\Resume\\hi.pdf'))
