with open('input.txt', 'r') as infile:
    lines = infile.readlines()
modified_lines = [line[::-1] for line in lines]
with open('output.txt', 'w') as outfile:
    outfile.writelines(modified_lines)
print("Success! Modified file 'output.txt' has been created.")
