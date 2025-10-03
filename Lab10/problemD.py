import os
import string

base_path = r"C:\Users\hlain\Downloads\Python-Lab10-Rev01"
dict_path = os.path.join(base_path, "dict.txt")

# Load dictionary
try:
    with open(dict_path, "r") as f:
        dictionary = {word.strip().lower() for line in f for word in line.split()}
except FileNotFoundError:
    print(f"Error: Dictionary file '{dict_path}' not found.")
    exit()

# Ask user for filename
filename = input("Enter a filename: ").strip()
file_path = os.path.join(base_path, filename)

try:
    with open(file_path, "r") as f:
        for line_number, line in enumerate(f, start=1):
            words = line.split()
            for word in words:
                clean_word_display = word.strip(string.punctuation)
                clean_word_lower = clean_word_display.lower()
                
                if clean_word_lower and clean_word_lower not in dictionary:
                    print(f"Line {line_number}: {clean_word_display}")
except FileNotFoundError:
    print("Error: Cannot open the file")
    exit()
