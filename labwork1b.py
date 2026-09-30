students = []
courses = []
marks = {}

def input_number_students():
    return int(input("Input number of students in a class: "))

def input_student_info():
    s_id = input("Student ID: ")
    name = input("Student Name: ")
    dob = input("Student DoB: ")
    students.append({"id": s_id, "name": name, "dob": dob})

def input_number_courses():
    return int(input("Input number of courses: "))

def input_course_info():
    c_id = input("Course ID: ")
    name = input("Course Name: ")
    courses.append({"id": c_id, "name": name})
    marks[c_id] = {}

def input_marks():
    list_courses()
    c_id = input("Select course ID: ")
    if any(c['id'] == c_id for c in courses):
        for s in students:
            mark = float(input(f"Input mark for student {s['name']}: "))
            marks[c_id][s['id']] = mark

def list_courses():
    for c in courses:
        print(f"Course: {c['id']} - {c['name']}")

def list_students():
    for s in students:
        print(f"Student: {s['id']} - {s['name']} - {s['dob']}")

def show_student_marks():
    c_id = input("Enter course ID to show marks: ")
    if c_id in marks:
        for s_id, mark in marks[c_id].items():
            name = next(s['name'] for s in students if s['id'] == s_id)
            print(f"{name}: {mark}")

if __name__ == "__main__":
    num_s = input_number_students()
    for _ in range(num_s): input_student_info()
    
    num_c = input_number_courses()
    for _ in range(num_c): input_course_info()
    
    input_marks()
    list_students()
    show_student_marks()