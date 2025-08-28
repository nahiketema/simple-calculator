def read_user_file():
    """
    Asks the user for a filename and reads its contents.
    Handles errors if the file doesn't exist or can't be read.
    """
    filename = input("Please enter the name of the file to read: ")
    
    try:
        # Open the file for reading
        with open(filename, 'r') as file:
            content = file.read()
            print("\n--- File Content ---")
            print(content)
            print("--------------------\n")
            
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist. Please check the name and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function
read_user_file()