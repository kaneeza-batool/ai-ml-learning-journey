students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

print(students)
print()
print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

for student in students:
    print(student)   # will just print the keys

print()
for student in students:
    print(student, students[student], sep=", ") 

print()
for student, place in students.items():
    print(student, place, sep=", ")
    
# list of disctionaries
students = [
    {
        "name": "Hermione",
        "house": "Gryyindor",
        "patronus": "Otter"
    },
    {
        "name": "Harry",
        "house": "Gryyindor",
        "patronus": "Stag"
    },
    {
        "name": "Ron",
        "house": "Gryyindor",
        "patronus": "Jack Russell terrier"
    },
    {
        "name": "Draco",
        "house": "Slytherin",
        "patronus": None
    }
]

print()
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")