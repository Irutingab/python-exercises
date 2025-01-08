def writetofile(filename, content):
    with open(filename, "w") as file:
        file.write(content)
        print(f"Content written to {filename}.")

def readfromfile(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(f"Content read from {filename}:")
            return content
    except FileNotFoundError:
        return f"Error: {filename} does not exist."

# Example 
filename = "example.txt"
content_to_write = """Good Morning, Students!
This is a simple read/write file example in Python."""

writetofile(filename, content_to_write)

file_content = readfromfile(filename)
print(file_content)
