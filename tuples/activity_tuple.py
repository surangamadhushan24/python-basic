students_tuple = (
    ("Alice", 22, 3.8, "Computer Science", ["Python", "Java", "SQL"]),
    ("Bob", 20, 3.5, "Mathematics", ["Python", "R"]),
    ("Charlie", 23, 3.7, "Physics", ["C", "Python"]),
    ("David", 24, 3.9, "Engineering", ["Java", "C++", "Python"]),
    ("Eve", 21, 3.6, "Biology", ["Python", "Excel"]),
    ("Frank", 25, 3.4, "Computer Science", ["C", "Java", "SQL"]),
    ("Grace", 22, 3.8, "Engineering", ["Python", "Java"]),
    ("Hannah", 26, 3.3, "Mathematics", ["C++", "Python"]),
    ("Ivy", 21, 3.9, "Computer Science", ["Python", "JavaScript"]),
    ("Jack", 23, 3.5, "Physics", ["Java", "SQL"]),
    ("Katie", 24, 3.7, "Engineering", ["Python", "C"]),
    ("Leo", 22, 3.8, "Mathematics", ["Java", "Python"]),
    ("Maya", 20, 3.6, "Biology", ["Excel", "Python"]),
    ("Nina", 23, 3.5, "Computer Science", ["JavaScript", "C++"]),
    ("Oscar", 25, 3.7, "Physics", ["C", "R"]),
    ("Paul", 22, 3.6, "Mathematics", ["Python", "R"]),
    ("Quincy", 24, 3.9, "Engineering", ["Python", "Java"]),
    ("Rachel", 21, 3.7, "Biology", ["JavaScript", "Python"]),
    ("Sam", 22, 3.5, "Computer Science", ["Java", "SQL"]),
    ("Tina", 26, 3.8, "Mathematics", ["Python", "Java"])
)

for student in students_tuple:
    if student[2] > 3.7 and student[3] == "Computer Science":
        print(student)

new_tuple = tuple(std[0] for std in students_tuple if student[2] >= 3.6 and "Python" in std[4])
print(new_tuple)

sum_of_gpa = sum(std[2] for std in students_tuple if std[3] == "Engineering")
count_of_engineering = len([std for std in students_tuple if std[3] == "Engineering"])

print(sum_of_gpa / count_of_engineering)

num_of_student_aged22 = tuple(std[0] for std in students_tuple if std[1] >= 22 and len(std[4]) >= 3)
print(num_of_student_aged22)
