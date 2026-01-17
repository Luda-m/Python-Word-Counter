print("----------------------------------")
print("         Word Counter             ")
print("----------------------------------")
filename = input("Enter the name of the file to open (e.g., words.txt): ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        
        words = content.split()
        
        word_count = len(words)
        
        print(f"The file '{filename}' has {word_count} words.")

except FileNotFoundError:
    print("Error: The file was not found. Please check the name is correct and try again!")