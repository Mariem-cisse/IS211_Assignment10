
import sqlite3

# Connect to the database
conn = sqlite3.connect("pets.db")
cursor = conn.cursor()

while True:
    person_id = input("Enter a person's ID (-1 to exit): ")

    if person_id == "-1":
        print("Goodbye!")
        break

    try:
        person_id = int(person_id)
    except ValueError:
        print("Please enter a valid ID number.")
        continue

    # Find the person
    cursor.execute("""
        SELECT first_name, last_name, age
        FROM person
        WHERE id = ?
    """, (person_id,))

    person = cursor.fetchone()

    if person:
        first_name, last_name, age = person

        print(f"{first_name} {last_name}, {age} years old")

        # Find the person's pets
        cursor.execute("""
            SELECT pet.name, pet.breed, pet.age
            FROM pet
            JOIN person_pet
            ON pet.id = person_pet.pet_id
            WHERE person_pet.person_id = ?
        """, (person_id,))

        pets = cursor.fetchall()

        for pet in pets:
            name, breed, pet_age = pet
            print(
                f"{first_name} {last_name} owned "
                f"{name}, a {breed}, that was {pet_age} years old."
            )
    else:
        print("Person not found.")

conn.close()
