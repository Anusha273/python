# Open the file in read mode
with open("emails.txt", 'r') as file:
    # Move the file pointer to a specific position (e.g., 10th byte)
    file.seek(10)  # Moves the pointer to the 10th position in the file
    
    # Read the content from the new pointer position
    content = file.read(20)  # Read 20 characters from the new position
    print(f"Content from position 10: {content}")

    # Get the current file pointer position
    position = file.tell()  # Returns the current file pointer position
    print(f"Current file pointer position: {position}")
