import shutil
import os

def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
        print(f"Content copied from '{source}' to '{destination}' successfully.")
    except FileNotFoundError:
        print(f"Error: '{source}' or '{destination}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def move_file(source, destination):
    try:
        shutil.move(source, destination)
        print(f"Content moved from '{source}' to '{destination}' successfully.")
    except FileNotFoundError:
        print(f"Error: '{source}' or '{destination}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def file_operations_menu():
    while True:
        print("\nFile Operations Menu:")
        print("1. Copy content of one file to another file")
        print("2. Move content of one file to another file")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            source = input("Enter the source file name: ")
            destination = input("Enter the destination file name: ")
            copy_file(source, destination)

        elif choice == '2':
            source = input("Enter the source file name: ")
            destination = input("Enter the destination file name: ")
            move_file(source, destination)

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice! Please choose again.")

# Run the file operations menu
file_operations_menu()
