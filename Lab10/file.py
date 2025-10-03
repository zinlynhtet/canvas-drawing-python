import os

base_path = r"C:\your\path\here"

old_file = os.path.join(base_path, "input.txt")
new_file = os.path.join(base_path, "output.txt")

with open(old_file, "r") as infile:
    lines = infile.readlines()

capitalized_lines = [line[0].upper() + line[1:] if line else "" for line in lines]

with open(old_file, "w") as outfile:
    outfile.writelines(capitalized_lines)

os.rename(old_file, new_file)

print("done")