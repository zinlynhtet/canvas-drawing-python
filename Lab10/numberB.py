filename = input("Enter the name of a text file: ")

try:
    with open(filename, "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("ERROR: File not found")