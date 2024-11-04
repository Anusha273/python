# Open the input file temps.txt for reading
input_file = open('temps.txt', 'r')
# Open the output file ftemps.txt for writing
output_file = open('ftemps.txt', 'w')

# Read each line from the input file, convert to Fahrenheit, and write to output file
for line in input_file:
    # Convert the temperature to Celsius (assuming each line contains a temperature in Celsius)
    celsius = float(line.strip())
    fahrenheit = (celsius * 9/5) + 32
    
    # Write the Fahrenheit temperature to the output file
    output_file.write(f"{fahrenheit}\n")

# Close the files
input_file.close()
output_file.close()
