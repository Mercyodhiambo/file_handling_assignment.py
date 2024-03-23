# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("This is line 1\n")
        file.write("12345\n")
        file.write("Another line with text and numbers: 987\n")
except PermissionError:
    print("Permission denied while creating the file.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("File creation process completed.")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        print("Content of my_file.txt:")
        print(file.read())
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("An error occurred:", e)

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("This is an appended line\n")
        file.write("67890\n")
        file.write("Appending more text: abc\n")
except PermissionError:
    print("Permission denied while appending to the file.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("File appending process completed.")
