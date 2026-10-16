from datetime import datetime

FILENAME = "notebook.txt"


def add_entry():
    text = input("Write your entry: ")
    time = datetime.now().strftime("%Y-%m-%D %H:%M:%S")
    with open(FILENAME, "a") as f:
        f.write(f"{text} \n {time}\n")   
    print(f"Entry added Successfully!\n{time}")


def view_entries():
    try:
        with open(FILENAME, "r") as f:
            content = f.read()
        if content.strip() == "":
            print("No Entries yet.")
        else:
            print(content)
    except FileNotFoundError:
        print("No Entries yet.")


def search_entries():
    word = input("What do you want to search? ")
    found = False
    try:
        with open(FILENAME, "r") as f:
            for line in f:
                if word.lower() in line.lower():
                    print(line, end="")
                    found = True
        if not found:
            print("No match found.")
    except FileNotFoundError:
        print("No Entries yet.")


def delete_entries():
    sure = input("Are you sure you want to delete everything? (yes/no): ")
    if sure.lower() == "yes":
        with open(FILENAME, "w"):       
            pass
        print("All entries deleted.")
    else:
        print("Cancelled.")


while True:
    print("\n1. Add Entry")
    print("2. View Entries")
    print("3. Search Entry")
    print("4. Delete All")
    print("5. Exit")

    choice = input("Your choice: ")

    if choice == "1":
        add_entry()
    elif choice == "2":
        view_entries()
    elif choice == "3":
        search_entries()
    elif choice == "4":
        delete_entries()
    elif choice == "5":
        print("Thank you for using the Journal! have a great day!")
        break
    else:
        print("Invalid choice, try again.")