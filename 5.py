# Function to count uppercase and lowercase characters in a file
def count_upper_lower(filename):
    with open(filename, 'r') as file:
        text = file.read()

    upper_count = 0
    lower_count = 0

    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

# Get the file path from user
filename = input("Enter the file name: ")

# Count uppercase and lowercase characters
upper, lower = count_upper_lower(filename)

# Display the results
print(f"Total uppercase characters: {upper}")
print(f"Total lowercase characters: {lower}")
