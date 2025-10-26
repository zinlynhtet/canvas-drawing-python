import os
import string

base_path = r"C:\your\path\here" 
dict_path = os.path.join(base_path, "dict.txt")

try:
    with open(dict_path, "r") as f:
        dictionary = {word.strip().lower() for line in f for word in line.split()}
except FileNotFoundError:
    print(f"Error: Dictionary file '{dict_path}' not found.")
    exit()

filename = input("Enter a filename: ").strip()
file_path = os.path.join(base_path, filename)

try:
    with open(file_path, "r") as f:
        for line_number, line in enumerate(f, start=1):
            words = line.split()
            for word in words:
                result = word.strip(string.punctuation)
                clean_word_lower = result.lower()
                
                if clean_word_lower and clean_word_lower not in dictionary:
                    print(f"Line {line_number}: {result}")
except FileNotFoundError:
    print("Error: Cannot open the file")
    exit()
