-- Create the 'instructors' table
CREATE TABLE instructors (
    instructor_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);

-- Create the 'courses' table
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    instructor_id INTEGER,
    FOREIGN KEY (instructor_id) REFERENCES instructors (instructor_id)
);

-- Create the 'students' table
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);

-- Create the 'enrollments' table
CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY,
    course_id INTEGER,
    student_id INTEGER,
    year INTEGER NOT NULL,
    grade INTEGER,
    FOREIGN KEY (course_id) REFERENCES courses (course_id),
    FOREIGN KEY (student_id) REFERENCES students (student_id)
);
