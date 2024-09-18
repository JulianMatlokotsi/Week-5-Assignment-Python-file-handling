# file_handling_assignment.py

def create_file():
    try:
        # Task 1: Create and write to a new file
        with open("my_file.txt", "w") as file:
            file.write("Hello! This is your personalized file.\n")
            file.write("Fun fact: The number 42 is often called 'the answer to life'\n")
            file.write("Third line: Keep going, you're doing great with Python!\n")
        print("Your file 'my_file.txt' has been created and personalised just for you.")

    except PermissionError:
        print("Oh oh! You don't have permission to create this file.")

    except Exception as e:
        print(f"Something unexpected happened: {e}")

def read_file():
    try:
        # Read the file and display contents
        with open("my_file.txt", "r") as file:
            contents = file.read()
            print("\nHere's what's inside your file:\n")
            print(contents)
        
    except FileNotFoundError:
        print("Oops! It seems like the file ins't here. Did you create it?")

    except Exception as e:
        print(f"An unexpected error occured: {e}")

def append_file():
    try:
        # Open the file in append mode and add more content
        with open("my_file.txt", "a") as file:
            file.write("you've made it this far. Keep up the good work!\n")
            file.write("Adding some extra numbers: 56 and 101.\n")
            file.write("Final Message: Never Stop Learning!\n")
        print("New lines have been added to your file. looking great!")
    except FileNotFoundError:
        print("Uhm, couldn't find the file to append. Are you sure it exists?")

    except Exception as e:
        print(f"Something went wrong: {e}")


def main():
    print("Starting file handling tasks...")
    try:
        create_file()   # Create and write initial content to file
        print("File creation complete. Now reading the file.")
        read_file()     # Read and display content
        print("Reading complete. Now appending to the file.")
        append_file()   # Append more content to file
        print("Appending complete. Final read to show updated file.")
        read_file()     # Read and display updated content
    finally:
        print("All operations completed successfully.")

if __name__ == "__main__":
    main()
