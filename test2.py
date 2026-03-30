import os

DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test.txt")


def save_name(name):
    clean_name = name.strip()
    if not clean_name:
        print("Name cannot be empty.")
        return

    with open(DB_FILE, "a", encoding="utf-8") as file:
        file.write(clean_name + "\n")

    print(f"Saved: {clean_name}")


while True:
    name = input("Enter a name (or 'exit' to quit): ").strip()

    if name.lower() == "exit":
        print("Done.")
        break

    save_name(name)