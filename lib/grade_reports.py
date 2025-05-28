#!/usr/bin/env python3
import os

def create_grade_report(student_grades):
    """
    Create a grade report file from a dictionary of student grades.
    The report is saved to 'reports/grade_report.txt'.
    """
    # Ensure the reports directory exists
    os.makedirs('reports', exist_ok=True)

    with open('reports/grade_report.txt', 'w') as gr:
        gr.write("Grade Report\n")
        gr.write("====================\n")
        for student, grade in student_grades.items():
            gr.write(f"{student}: {grade}\n")

def get_student_grades_from_input():
    """
    Prompt the user to enter multiple student grades.
    Input format: "StudentName Grade"
    Enter an empty line to finish.
    Returns a dictionary of student grades.
    """
    print("Enter student grades (name and grade separated by space). Enter an empty line to finish:")
    grades = {}
    while True:
        try:
            entry = input()
        except EOFError:
            print("\nInput terminated.")
            break
        if not entry.strip():
            break
        try:
            student, grade = entry.split(maxsplit=1)
            grades[student] = grade
        except ValueError:
            print("Invalid input format. Please enter in 'StudentName Grade' format.")
    return grades

if __name__ == '__main__':
    student_grades = get_student_grades_from_input()
    if student_grades:
        create_grade_report(student_grades)
        print("Grade report created successfully in 'reports/grade_report.txt'.")
    else:
        print("No student grades entered. Grade report not created.")
