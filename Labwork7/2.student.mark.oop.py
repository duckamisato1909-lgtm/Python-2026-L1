import math
import numpy as np

class Student:
    def __init__(self, s_id, name, dob):
        self.__id = s_id
        self.__name = name
        self.__dob = dob
        self.__marks = {} 

    # Getters
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def get_marks(self):
        return self.__marks

    def add_mark(self, course_id, mark):
        self.__marks[course_id] = math.floor(mark * 10) / 10

    def calculate_gpa(self, courses):
        course_marks = []
        course_credits = []
        for c in courses:
            c_id = c.get_id()
            if c_id in self.__marks:
                course_marks.append(self.__marks[c_id])
                course_credits.append(c.get_credits())
        
        if not course_marks:
            return 0.0
        
        marks_arr = np.array(course_marks, dtype=float)
        credits_arr = np.array(course_credits, dtype=float)
        total_credits = np.sum(credits_arr)
        
        if total_credits == 0:
            return 0.0
        return float(np.sum(marks_arr * credits_arr) / total_credits)

    def describe(self):
        return f"Student ID: {self.__id} | Name: {self.__name} | DoB: {self.__dob}"


class Course:
    def __init__(self, c_id, name, credits):
        self.__id = c_id
        self.__name = name
        self.__credits = credits

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_credits(self):
        return self.__credits

    def describe(self):
        return f"Course: {self.__id} - {self.__name} ({self.__credits} credits)"


class SchoolManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_data(self):
        num_s = int(input("Input number of students in a class: "))
        for _ in range(num_s):
            s_id = input("Student ID: ")
            name = input("Student Name: ")
            dob = input("Student DoB: ")
            self.students.append(Student(s_id, name, dob))

        num_c = int(input("Input number of courses: "))
        for _ in range(num_c):
            c_id = input("Course ID: ")
            name = input("Course Name: ")
            credits = int(input(f"Input credits for course {name}: "))
            self.courses.append(Course(c_id, name, credits))

        for c in self.courses:
            print(f"\nInput marks for course: {c.get_name()} ({c.get_id()})")
            for s in self.students:
                mark = float(input(f"Input mark for student {s.get_name()}: "))
                s.add_mark(c.get_id(), mark)

    def list_students(self):
        print("\n--- Student List ---")
        for s in self.students:
            print(s.describe())

    def list_courses(self):
        print("\n--- Course List ---")
        for c in self.courses:
            print(c.describe())

    def show_student_gpas(self):
        print("\n--- Students Sorted by GPA ---")
        if not self.students:
            return
        
        # Tính GPA và sắp xếp giảm dần bằng numpy
        student_gpas = [(s, s.calculate_gpa(self.courses)) for s in self.students]
        student_gpas.sort(key=lambda x: x[1], reverse=True)
        
        for s, gpa in student_gpas:
            print(f"ID: {s.get_id()} | Name: {s.get_name()} | GPA: {gpa:.2f}")


if __name__ == "__main__":
    system = SchoolManagementSystem()
    system.input_data()
    system.list_courses()
    system.list_students()
    system.show_student_gpas()