students = {
    "Alice": {"Age": 22, "GPA": 3.8},
    "Bob": {"Age": 20, "GPA": 3.5},
    "Eric": {"Age": 25, "GPA": 3.6},
    "David": {"Age": 23, "GPA": 3.7},
    "Sophia": {"Age": 21, "GPA": 3.9},
    "James": {"Age": 24, "GPA": 3.4},
    "Olivia": {"Age": 22, "GPA": 3.8},
    "Michael": {"Age": 26, "GPA": 3.3},
    "Emma": {"Age": 20, "GPA": 3.7},
    "Daniel": {"Age": 23, "GPA": 3.6},
    "Ava": {"Age": 21, "GPA": 3.9},
    "Ethan": {"Age": 24, "GPA": 3.5},
    "Mia": {"Age": 22, "GPA": 3.8},
    "Matthew": {"Age": 25, "GPA": 3.4},
    "Charlotte": {"Age": 20, "GPA": 3.7},
    "Benjamin": {"Age": 23, "GPA": 3.6},
    "Amelia": {"Age": 21, "GPA": 3.9},
    "William": {"Age": 22, "GPA": 3.5},
    "Harper": {"Age": 24, "GPA": 3.8},
    "Lucas": {"Age": 23, "GPA": 3.6}
}

count =0

for std in students:
    if std[0].lower().startswith("m"):
        count += 1

print(count)

for items in students.items():
    if items[1]["Age"] > 24:
        print(items[0])


print(sum(student["GPA"] for student in students.values())/len(students))

max_gpa = max(student["GPA"] for student in students.values())

top_students = {name: details["GPA"] for name, details in students.items() if details["GPA"] == max_gpa}

print("Top Students:")
for name, gpa in top_students.items():
    print(f"{name}: {gpa}")



