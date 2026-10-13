import math
import numpy as np
import curses

students = []
courses = []
marks = {} 


def input_number_students():
    while True:
        try:
            n = int(input("Input number of students in a class: "))
            if n < 1:
                print("Number of students must be greater than 0.")
                continue
            return n
        except ValueError:
            print("Please enter a valid integer.")


def input_student_info():
    while True:
        s_id = input("Student ID: ").strip()
        if not s_id:
            print("Student ID cannot be empty.")
        elif any(s["id"] == s_id for s in students):
            print("Student ID already exists.")
        else:
            break

    name = input("Student Name: ").strip()
    dob = input("Student DoB (DD/MM/YYYY): ").strip()

    students.append({
        "id": s_id,
        "name": name,
        "dob": dob
    })


def input_number_courses():
    while True:
        try:
            n = int(input("Input number of courses: "))
            if n < 1:
                print("Number of courses must be greater than 0.")
                continue
            return n
        except ValueError:
            print("Please enter a valid integer.")


def input_course_info():
    while True:
        c_id = input("Course ID: ").strip()
        if not c_id:
            print("Course ID cannot be empty.")
        elif any(c["id"] == c_id for c in courses):
            print("Course ID already exists.")
        else:
            break

    name = input("Course Name: ").strip()

    while True:
        try:
            credits = int(input(f"Input credits for course {name}: "))
            if credits <= 0:
                print("Credits must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    courses.append({
        "id": c_id,
        "name": name,
        "credits": credits
    })

    marks[c_id] = {}


def list_courses():
    print("\n--- Course List ---")
    for c in courses:
        print(
            f"ID: {c['id']} | "
            f"Name: {c['name']} | "
            f"Credits: {c['credits']}"
        )


def input_marks():
    for c in courses:
        print(f"\n--- Enter marks for {c['name']} ({c['id']}) ---")

        for s in students:
            while True:
                try:
                    raw_mark = float(
                        input(f"Input mark for student {s['name']}: ")
                    )

                    if not 0 <= raw_mark <= 10:
                        print("Mark must be between 0 and 10.")
                        continue

                    # Round down to one decimal place
                    mark = math.floor(raw_mark * 10) / 10
                    marks[c["id"]][s["id"]] = mark
                    break

                except ValueError:
                    print("Please enter a valid number.")


def calculate_gpa(s_id):
    course_marks = []
    course_credits = []

    for c in courses:
        c_id = c["id"]

        if s_id in marks.get(c_id, {}):
            course_marks.append(marks[c_id][s_id])
            course_credits.append(c["credits"])

    if not course_marks:
        return 0.0

    marks_arr = np.array(course_marks, dtype=float)
    credits_arr = np.array(course_credits, dtype=float)

    total_credits = np.sum(credits_arr)

    if total_credits == 0:
        return 0.0

    gpa = np.sum(marks_arr * credits_arr) / total_credits
    return float(gpa)


def sort_students_by_gpa():
    if not students:
        return []

    student_gpas = []

    for s in students:
        gpa = calculate_gpa(s["id"])
        student_gpas.append(gpa)

    gpa_arr = np.array(student_gpas, dtype=float)
    sorted_indices = np.argsort(gpa_arr)[::-1]

    sorted_list = [
        (students[i], gpa_arr[i])
        for i in sorted_indices
    ]

    return sorted_list


def display_with_curses(stdscr):
    curses.start_color()
    curses.use_default_colors()

    curses.init_pair(1, curses.COLOR_CYAN, -1)
    curses.init_pair(2, curses.COLOR_GREEN, -1)

    stdscr.clear()
    h, w = stdscr.getmaxyx()

    title = "=== STUDENT MANAGEMENT SYSTEM - GPA & RANKING ==="

    title_x = max(0, (w - len(title)) // 2)
    stdscr.addstr(
        1, title_x, title[:max(0, w - title_x - 1)],
        curses.color_pair(1) | curses.A_BOLD
    )

    sorted_students = sort_students_by_gpa()

    row = 3
    header = f"{'ID':<10} {'Name':<20} {'DoB':<15} {'GPA':<10}"

    if row < h - 1:
        stdscr.addstr(
            row, 2, header[:max(0, w - 3)],
            curses.A_UNDERLINE
        )
    row += 1

    for item, gpa in sorted_students:
        if row >= h - 3:
            break

        line = (
            f"{item['id']:<10} "
            f"{item['name']:<20} "
            f"{item['dob']:<15} "
            f"{gpa:<10.2f}"
        )

        stdscr.addstr(
            row, 2, line[:max(0, w - 3)],
            curses.color_pair(2)
        )
        row += 1

    if h >= 2:
        message = "Press any key to exit..."
        stdscr.addstr(
            h - 1, 0, message[:max(0, w - 1)]
        )

    stdscr.refresh()
    stdscr.getch()


def display_console():
    print("\n--- Student List Sorted by GPA ---")

    sorted_students = sort_students_by_gpa()

    if not sorted_students:
        print("No students available.")
        return

    print(f"{'ID':<12} {'Name':<25} {'DoB':<15} {'GPA':<10}")
    print("-" * 62)

    for item, gpa in sorted_students:
        print(
            f"{item['id']:<12} "
            f"{item['name']:<25} "
            f"{item['dob']:<15} "
            f"{gpa:<10.2f}"
        )


if __name__ == "__main__":
    try:
        num_s = input_number_students()

        for _ in range(num_s):
            print("\nEnter student information:")
            input_student_info()

        num_c = input_number_courses()

        for _ in range(num_c):
            print("\nEnter course information:")
            input_course_info()

        input_marks()

        try:
            curses.wrapper(display_with_curses)

        except Exception as e:
            print(f"\nCurses display unavailable: {e}")
            display_console()

    except (KeyboardInterrupt, EOFError):
        print("\nProgram terminated.")