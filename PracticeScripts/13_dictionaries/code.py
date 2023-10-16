friend_ages = {"Rolf": 24, "Adam":30, "Anne": 27}

friend_ages["Rolf"] = 20

print(friend_ages)

friends = [
    {"name": "Rolf", "age": 23},
    {"name": "Lee", "age": 24},
    {"name": "Andy", "age": 26},
    {"name": "Brit", "age": 24},
    ]

print(friends[1]["name"])

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

for student in student_attendance:
    print(f"{student}: {student_attendance[student]}")

print("\n better way to do this would be:")

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

if "Bob" in student_attendance:
    print(f"Bob: {student_attendance['Bob']}")
else:
    print("Bob is not a student in this class.")