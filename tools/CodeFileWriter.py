from langchain.tools import tool
import os

class CodeFileWriter:

    @tool("rewrite_code_file")
    def rewrite_code_file(file_path: str, new_content: str) -> str:
        """
        Useful to Overwrites the specified file with new content.
        
        Parameters:
        - file_path (str): The absolute path of the file to rewrite.
        - new_content (str): The full content to write to the file, representing the finalized code with improvements.

        Returns:
        - A message confirming the operation success or failure.
        """
        try:
            # Check if file exists
            if not os.path.exists(file_path):
                return f"Error: The file '{file_path}' does not exist."

            # Write the new content to the file, replacing its current content
            with open(file_path, 'w') as file:
                file.write(new_content)

            return f"File '{file_path}' successfully rewritten with new content."

        except Exception as e:
            return f"Error writing to the file: {e}"

