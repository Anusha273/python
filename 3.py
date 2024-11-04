# Open the file in read mode
with open('3.txt', 'r') as file:
    # Initialize a counter
    line_count = 0
    
    # Loop through each line in the file
    for line in file:
        line_count += 1  # Increment the counter for each line

# Print the total count of lines
print("Number of lines:", line_count)

