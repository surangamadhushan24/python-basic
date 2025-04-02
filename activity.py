students_data = [
    {"name": "Alice", "age": 22, "GPA": 3.8, "major": "Computer Science", "skills": ["Python", "Java", "SQL"]},
    {"name": "Bob", "age": 20, "GPA": 3.5, "major": "Mathematics", "skills": ["Python", "R"]},
    {"name": "Charlie", "age": 23, "GPA": 3.7, "major": "Physics", "skills": ["C", "Python"]},
    {"name": "David", "age": 24, "GPA": 3.9, "major": "Engineering", "skills": ["Java", "C++", "Python"]},
    {"name": "Eve", "age": 21, "GPA": 3.6, "major": "Biology", "skills": ["Python", "Excel"]},
    {"name": "Frank", "age": 25, "GPA": 3.4, "major": "Computer Science", "skills": ["C", "Java", "SQL"]},
    {"name": "Grace", "age": 22, "GPA": 3.8, "major": "Engineering", "skills": ["Python", "Java"]},
    {"name": "Hannah", "age": 26, "GPA": 3.3, "major": "Mathematics", "skills": ["C++", "Python"]},
    {"name": "Ivy", "age": 21, "GPA": 3.9, "major": "Computer Science", "skills": ["Python", "JavaScript"]},
    {"name": "Jack", "age": 23, "GPA": 3.5, "major": "Physics", "skills": ["Java", "SQL"]},
    {"name": "Katie", "age": 24, "GPA": 3.7, "major": "Engineering", "skills": ["Python", "C"]},
    {"name": "Leo", "age": 22, "GPA": 3.8, "major": "Mathematics", "skills": ["Java", "Python"]},
    {"name": "Maya", "age": 20, "GPA": 3.6, "major": "Biology", "skills": ["Excel", "Python"]},
    {"name": "Nina", "age": 23, "GPA": 3.5, "major": "Computer Science", "skills": ["JavaScript", "C++"]},
    {"name": "Oscar", "age": 25, "GPA": 3.7, "major": "Physics", "skills": ["C", "R"]},
    {"name": "Paul", "age": 22, "GPA": 3.6, "major": "Mathematics", "skills": ["Python", "R"]},
    {"name": "Quincy", "age": 24, "GPA": 3.9, "major": "Engineering", "skills": ["Python", "Java"]},
    {"name": "Rachel", "age": 21, "GPA": 3.7, "major": "Biology", "skills": ["JavaScript", "Python"]},
    {"name": "Sam", "age": 22, "GPA": 3.5, "major": "Computer Science", "skills": ["Java", "SQL"]},
    {"name": "Tina", "age": 26, "GPA": 3.8, "major": "Mathematics", "skills": ["Python", "Java"]},
]

for student in students_data:
    if student["major"] == "Computer Science" and student["GPA"] >= 3.7:
        print(student["name"])

# for student in students_data:
#     if len(student["skills"]) == 3:
#         print(student["name"])

skills_students = [std["name"] for std in students_data if len(std["skills"]) == 3]
print(skills_students)

for student in students_data:
    if student["GPA"] == max(s["GPA"] for s in students_data):
        print(student)

tot_avg = 0
count = 0
for student in students_data:
    if student["major"] == "Engineering":
        tot_avg += float(student["GPA"])
        count += 1

print(tot_avg / count)

# for student in students_data:
#     if student["age"] >= 22 and student["skills"] in :

older_than22_python_skills = [std for std in students_data if std["age"] > 22 and "Python" in std["skills"]]
print(older_than22_python_skills)

python_and_gpa = [std["name"] for std in students_data if "Python" in std["skills"] and std["GPA"] > 3.5]
print(f"python and gpa grater than 3.5{python_and_gpa}")

# max_skills = max(for std in students_data)
# most_skilled_students = [std for std in students_data if len(std["skills"]) == max_skills]
# print(f"most skills students are {most_skilled_students}")

# all_student_count = len(students_data)
# gpa_highest_students = len(std for std in students_data if student["GPA"] >= 3.7)
# persenatge = (gpa_highest_students/all_student_count) * 100
# print(persenatge)
