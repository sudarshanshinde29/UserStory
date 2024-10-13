from langchain.tools import tool
import os
class CodeFileManager():
    
    @tool("create_code_file")
    def create_code_file(file_path: str) -> str:
        """
        Creates a new file at the specified path if that particuler test file does not already exist.
        Parameters:
        - file_path (str): The absolute path where the new file should be created.
        Returns:
        - The complete path of the created file.
        """
        try:
            # Create the directories if they don't exist
            directory = os.path.dirname(file_path)
            if not os.path.exists(directory):
                os.makedirs(directory)
            
            # Check if the file already exists
            if not os.path.exists(file_path):
                # Create the file
                with open(file_path, 'w') as file:
                    pass  # Create an empty file
                return f"File created successfully at: {os.path.abspath(file_path)}"
            else:
                return f"File already exists at: {os.path.abspath(file_path)}"
        except Exception as e:
            return f"Error creating the file: {e}"