def handle_file():
    """
    Creates a text file, writes content, reads it, appends more content,
    and handles potential file-related exceptions.
    """

    try:
        # Create the file in write mode
        with open("my_file.txt", "w") as file:
            file.write("Line 1: This is some text.\n")
            file.write("Line 2: Here are some numbers: 10, 20, 30.\n")
            file.write("Line 3: And a mix of both!\n")

        # Read the file contents
        with open("my_file.txt", "r") as file:
            contents = file.read()
            print("File contents:\n", contents)

        # Append additional content
        with open("my_file.txt", "a") as file:
            file.write("\nLine 4: Appending more text.\n")
            file.write("Line 5: This is some additional content.\n")
            file.write("Line 6: The file has been modified.\n")

        print("\nSuccessfully created, read from, and appended to 'my_file.txt'.")

    except FileNotFoundError:
        print("Error: The file 'my_file.txt' does not exist.")
    except PermissionError:
        print("Error: You don't have permission to access or modify the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\nFile handling operations completed.")

if __name__ == "__main__":
    handle_file()


