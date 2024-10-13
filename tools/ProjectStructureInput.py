import os
from langchain.tools import tool

class ProjectStructureInput():
    
    @tool("get_project_structure")
    def get_project_structure(project_directory: str, file_name: str = None) -> str:
        """
        Retrieves and displays the directory structure of a specified project directory, including the
        full path of each file and folder. If a file name is provided, it returns the path(s) of the file(s) 
        that match the given name, considering both files with and without extensions.

        Parameters:
        - project_directory (str): The absolute path to the root of the project directory.
        - file_name (str, optional): The name of the file to search for (with or without extension). 
                                     If provided, only matching files will be returned.

        Returns:
        - A string representation of the matching file paths or the entire project directory structure.
        """
        try:
            # Validate if the provided directory exists
            if not os.path.exists(project_directory):
                return f"Error: The directory '{project_directory}' does not exist."

            # Function to recursively list directory structure or search for the file
            def list_dir_structure(dir_path, target_file=None, indent_level=0):
                structure = ""
                for item in os.listdir(dir_path):
                    item_path = os.path.join(dir_path, item)
                    # Extract file name without extension for comparison
                    base_name, ext = os.path.splitext(item)

                    if os.path.isdir(item_path):
                        structure += list_dir_structure(item_path, target_file, indent_level + 1)
                    elif os.path.isfile(item_path):
                        # If target_file is provided, check for a match with or without extension
                        if target_file and (base_name == target_file or item == target_file):
                            structure += f"- {item} (Path: {item_path})\n"
                        # If no target_file is provided, return the full structure
                        elif not target_file:
                            structure += "    " * indent_level + f"- {item} (Path: {item_path})\n"
                return structure

            # If a file name is provided, search for the file in the project directory
            if file_name:
                matching_files = list_dir_structure(project_directory, file_name)
                if matching_files:
                    return f"Matching files with name '{file_name}' in '{project_directory}':\n\n{matching_files}"
                else:
                    return f"No files with the name '{file_name}' found in the directory '{project_directory}'."

            # If no file name is provided, return the full directory structure
            project_structure = f"Directory structure of '{project_directory}':\n\n"
            project_structure += list_dir_structure(project_directory)

            return project_structure

        except Exception as e:
            return f"Error retrieving the project structure: {e}"
