# Open the file in read mode
with open(f"emails.txt", 'r') as file:
    # Read all lines from the file
    emails = file.readlines()

# Strip newline characters and join the emails with semicolons
email_string = ";".join(email.strip() for email in emails)

# Print the resulting string
print(email_string)
