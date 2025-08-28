# Create a dummy file for the program to read
with open('original.txt', 'w') as file:
    file.write("This is a test sentence.\n")
    file.write("Another line to demonstrate file reading.")

def modify_and_write_file(input_filename, output_filename):
    """
    Reads a file, modifies its content, and writes it to a new file.
    
    Args:
        input_filename (str): The name of the file to read.
        output_filename (str): The name of the file to write to.
    """
    try:
        # Open the input file for reading
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Modify the content (e.g., make it all uppercase)
        modified_content = content.upper()
        
        # Open the output file for writing
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
            
        print(f"Successfully modified '{input_filename}' and saved to '{output_filename}'.")
        
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function with your filenames
modify_and_write_file('original.txt', 'modified.txt')