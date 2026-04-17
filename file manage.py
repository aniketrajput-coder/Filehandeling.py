import os

def create_file():
    filename = input("Enter file name (with extension): ")
    file = open(filename, "w")
    file.close()
    print("File created successfully")

def write_file():
    filename = input("Enter file name to write: ")
    data = input("Enter data: ")
    file = open(filename, "w")
    file.write(data)
    file.close()
    print("Data written successfully")

def append_file():
    filename = input("Enter file name to append: ")
    data = input("Enter data to add: ")
    file = open(filename, "a")
    file.write("\n" + data)
    file.close()
    print("Data appended successfully")

def read_file():
    filename = input("Enter file name to read: ")
    file = open(filename, "r")
    content = file.read()
    print("File Content:\n", content)
    file.close()

def delete_file():
    filename = input("Enter file name to delete: ")
    if os.path.exists(filename):
        os.remove(filename)
        print("File deleted successfully")
    else:
        print("File does not exist")

# Menu system
while True:
    print("--- File Management System ---")
    print("1. Create File")
    print("2. Write File")
    print("3. Append File")
    print("4. Read File")
    print("5. Delete File")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_file()
    elif choice == "2":
        write_file()
    elif choice == "3":
        append_file()
    elif choice == "4":
        read_file()
    elif choice == "5":
        delete_file()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice")