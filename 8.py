def append_to_file(filename, new_data):
    try:
        # Open the file in append mode
        with open(filename, 'a') as file:
            # Append the new data to the file
            file.write(new_data + '\n')
            print(f"Data has been appended to '{filename}' successfully.")
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
filename = input("Enter the file name: ")
new_data = input("Enter the data to append: ")
append_to_file(filename, new_data)
