import sqlite3

# Connect to the database
conn = sqlite3.connect("pets.db")
cursor = conn.cursor()

# Create the person table
cursor.execute("""
CREATE TABLE IF NOT EXISTS person (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER
)
""")

# Create the pet table
cursor.execute("""
CREATE TABLE IF NOT EXISTS pet (
    id INTEGER PRIMARY KEY,
    name TEXT,
    breed TEXT,
    age INTEGER,
    dead INTEGER
)
""")

# Create the person_pet table
cursor.execute("""
CREATE TABLE IF NOT EXISTS person_pet (
    person_id INTEGER,
    pet_id INTEGER
)
""")

# Insert people
people = [
    (1, 'James', 'Smith', 41),
    (2, 'Diana', 'Greene', 23),
    (3, 'Sara', 'White', 27),
    (4, 'William', 'Gibson', 23)
]

cursor.executemany(
    "INSERT OR IGNORE INTO person VALUES (?, ?, ?, ?)",
    people
)

# Insert pets
pets = [
    (1, 'Rusty', 'Dalmation', 4, 1),
    (2, 'Bella', 'Alaskan Malamute', 3, 0),
    (3, 'Max', 'Cocker Spaniel', 1, 0),
    (4, 'Rocky', 'Beagle', 7, 0),
    (5, 'Rufus', 'Cocker Spaniel', 1, 0),
    (6, 'Spot', 'Bloodhound', 2, 1)
]

cursor.executemany(
    "INSERT OR IGNORE INTO pet VALUES (?, ?, ?, ?, ?)",
    pets
)

# Connect people to pets
relationships = [
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (4, 6)
]

cursor.executemany(
    "INSERT OR IGNORE INTO person_pet VALUES (?, ?)",
    relationships
)

# Save changes
conn.commit()
conn.close()

print("Pets database successfully loaded!")
