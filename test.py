# Read the file
with open('input.txt', 'r') as file:
    content = file.readlines()

# Define the indentation pattern
indentation = "&nbsp; &nbsp; "

# Iterate through each line and apply replacements
output = ""
for line in content:
    line ='<p>'+line
    line = line.replace("    ", "&nbsp; &nbsp; ")
    line = line.strip()+'</p>\n'
    print(line)
    output += line

# Write the modified content to a new file
with open('output.txt', 'w') as file:
    file.write(output)
