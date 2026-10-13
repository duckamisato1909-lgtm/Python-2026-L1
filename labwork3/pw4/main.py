from input import (
    input_number_students, input_student_info,
    input_number_courses, input_course_info, input_marks
)
from output import display_with_curses

def main():
    students = []
    courses = []
    marks = {}

    num_s = input_number_students()
    for _ in range(num_s):
        students.append(input_student_info())

    num_c = input_number_courses()
    for _ in range(num_c):
        courses.append(input_course_info())

    c_id, c_marks = input_marks(students, courses)
    marks[c_id] = c_marks

    display_with_curses(students, courses, marks)

if __name__ == "__main__":
    main()
