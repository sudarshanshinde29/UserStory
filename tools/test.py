import os
project_directory = 'WebGoat'
file_name = 'MenuController'  # Specify the file name without the extension

if not os.path.exists(project_directory):
    print(f"Error: The directory '{project_directory}' does not exist.")

# Function to recursively search and list full paths of matching file names, considering files with and without extensions
def list_matching_files(dir_path, target_file, indent_level=0):
    matching_files = ""
    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        # Extract file name without extension for comparison
        base_name, ext = os.path.splitext(item)
        if os.path.isdir(item_path):
            # Recurse into subdirectories
            matching_files += list_matching_files(item_path, target_file, indent_level + 1)
        elif os.path.isfile(item_path) and (base_name == target_file or item == target_file):
            # If the item matches the target file name (with or without extension)
            matching_files += "    " * indent_level + f"- {item} (Path: {item_path})\n"
    return matching_files

# Search for the specified file name in the project directory
project_structure = f"Matching files with name '{file_name}' in '{project_directory}':\n\n"
project_structure += list_matching_files(project_directory, file_name)

# Print the matching file paths
if project_structure.strip():
    print(project_structure)
else:
    print(f"No files with the name '{file_name}' found in the directory '{project_directory}'.")
