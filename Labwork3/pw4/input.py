import math
from domains.student import Student
from domains.course import Course

def input_number_students():
    return int(input("Input number of students in a class: "))

def input_student_info():
    s_id = input("Student ID: ")
    name = input("Student Name: ")
    dob = input("Student DoB: ")
    return Student(s_id, name, dob)

def input_number_courses():
    return int(input("Input number of courses: "))

def input_course_info():
    c_id = input("Course ID: ")
    name = input("Course Name: ")
    credits = int(input(f"Input credits for course {name}: "))
    return Course(c_id, name, credits)

def input_marks(students, courses):
    for c in courses:
        print(f"Course: {c.get_id()} - {c.get_name()}")
    
    c_id = input("Select course ID to input marks: ")
    marks_dict = {}
    for s in students:
        raw_mark = float(input(f"Input mark for student {s.get_name()}: "))
        mark = math.floor(raw_mark * 10) / 10
        marks_dict[s.get_id()] = mark
    return c_id, marks_dict