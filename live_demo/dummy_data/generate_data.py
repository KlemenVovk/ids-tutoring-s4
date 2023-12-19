import random
import json


# Names sampled from https://github.com/rossgoodwin/american-names/tree/master

# Sample data
n_students = 500
random.seed(1)
courses = ["Programming 1", "Programming 2", "Computer Architecture", "Operating Systems", "Data Structures", "Algorithms", "Computer Networks", "Databases", "Software Engineering", "Computer Graphics", "Artificial Intelligence", "Machine Learning", "Computer Vision", "Robotics", "Computer Security", "Cryptography", "Computer Vision", "Natural Language Processing", "Computer Music", "Computer Animation"]


first_names = []
with open('first_names.json') as f:
    first_names = json.load(f)

last_names = []
with open('last_names.json') as f:
    last_names = json.load(f)

# Generate random data for instructors, courses, students
instructors_data = [(random.choice(first_names), random.choice(last_names)) for _ in range(len(courses))]
courses_data = [(course, instructor_id + 1) for instructor_id, course in enumerate(courses)]
students_data = [(random.choice(first_names), random.choice(last_names)) for _ in range(n_students)]
years = list(range(2015, 2024))

# Generate INSERT statements for 'instructors'
insert_instructors = "\n".join(
    f"INSERT INTO instructors (first_name, last_name) VALUES ('{fname}', '{lname}');"
    for fname, lname in instructors_data
)

# Generate INSERT statements for 'courses'
insert_courses = "\n".join(
    f"INSERT INTO courses (name, instructor_id) VALUES ('{name}', {instructor_id});"
    for name, instructor_id in courses_data
)

# Generate INSERT statements for 'students'
insert_students = "\n".join(
    f"INSERT INTO students (first_name, last_name) VALUES ('{fname}', '{lname}');"
    for fname, lname in students_data
)

# Generate INSERT statements for 'enrollments'
insert_enrollments = "\n".join(
    f"INSERT INTO enrollments (student_id, course_id, year, grade) VALUES ({student_id}, {course_id}, {random.randint(2020,2023)}, {random.randint(6, 10) if random.random() < 0.8 else "NULL"});"
    for student_id, (_, _) in enumerate(students_data, 1)
    for course_id, (_, _) in enumerate(courses_data[:-2], 1) # 2 courses are new and have no enrollments yet
    if random.random() < 0.5
)

with open('populatedb.sql', 'w') as f:
    f.write(insert_instructors + "\n\n")
    f.write(insert_courses + "\n\n")
    f.write(insert_students + "\n\n")
    f.write(insert_enrollments + "\n\n")
