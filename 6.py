# Simple program to delete a file using os.remove()
import os

filename = input("Enter the file name to delete: ")

try:
    os.remove(filename)  # This deletes the file
    print(f"{filename} has been deleted successfully.")
except FileNotFoundError:
    print(f"{filename} not found.")
except Exception as e:
    print(f"Error: {e}")
