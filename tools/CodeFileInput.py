from langchain.tools import tool

class CodeFileInput():

    @tool("retrieve_code_file")
    def retrieve_code_file(code_file: str) -> str:
        """
        Retrieves the content of a specified code file.
        Parameters:
        - code_file (str): The path to the code file to be retrieve.
        Returns:
        - A string representation of the file content.
        """
        try:
            # Open and read the file content
            with open(code_file, 'r') as file:
                content = file.read()
            return f"Content of '{code_file}':\n\n{content}"
        except FileNotFoundError:
            return f"Error: The file '{code_file}' does not exist."
        except Exception as e:
            return f"Error reading the file: {e}"
