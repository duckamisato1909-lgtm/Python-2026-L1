import curses
import numpy as np

def calculate_gpa(student, courses, marks):
    s_id = student.get_id()
    course_marks = []
    course_credits = []
    
    for c in courses:
        c_id = c.get_id()
        if c_id in marks and s_id in marks[c_id]:
            course_marks.append(marks[c_id][s_id])
            course_credits.append(c.get_credits())
            
    if not course_marks:
        return 0.0
        
    marks_arr = np.array(course_marks, dtype=float)
    credits_arr = np.array(course_credits, dtype=float)
    total_credits = np.sum(credits_arr)
    
    if total_credits == 0:
        return 0.0
    return float(np.sum(marks_arr * credits_arr) / total_credits)

def sort_students(students, courses, marks):
    if not students:
        return []
    gpas = [calculate_gpa(s, courses, marks) for s in students]
    gpa_arr = np.array(gpas)
    sorted_indices = np.argsort(gpa_arr)[::-1]
    return [(students[i], gpa_arr[i]) for i in sorted_indices]

def display_with_curses(students, courses, marks):
    def _draw(stdscr):
        curses.start_color()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        
        title = "=== STUDENT MANAGEMENT SYSTEM (PW8 - MULTITHREADED) ==="
        stdscr.addstr(1, max(0, (w - len(title)) // 2), title, curses.color_1 | curses.A_BOLD)
        
        sorted_list = sort_students(students, courses, marks)
        
        row = 3
        stdscr.addstr(row, 2, f"{'ID':<10} {'Name':<20} {'DoB':<15} {'GPA':<10}", curses.A_UNDERLINE)
        row += 1
        
        for student, gpa in sorted_list:
            line = f"{student.get_id():<10} {student.get_name():<20} {student.get_dob():<15} {gpa:<10.2f}"
            stdscr.addstr(row, 2, line, curses.color_2)
            row += 1
            
        stdscr.addstr(row + 2, 2, "Press any key to exit...")
        stdscr.refresh()
        stdscr.getch()

    try:
        curses.wrapper(_draw)
    except Exception as e:
        print(f"Curses error: {e}")
        print("\n--- Student List Sorted by GPA ---")
        for student, gpa in sort_students(students, courses, marks):
            print(f"ID: {student.get_id()} | Name: {student.get_name()} | GPA: {gpa:.2f}")