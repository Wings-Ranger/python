import os

DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test.txt")

def write_person(first, last):
    full = first + " " + last
    existing = read_all()
    if full not in existing:
        with open(DB_FILE, "a") as f:
            f.write(full + "\n")
    else:
        print(f"{full} is already in the file.")

def read_all():
    try:
        with open(DB_FILE, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("The file does not exist.")
        return []

# --- Main ---
nameFirst = "Lachlan"
nameLast = "Nash"

write_person(nameFirst, nameLast)

print("All done!")
for name in read_all():
    print(name)