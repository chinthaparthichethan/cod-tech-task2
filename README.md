## Student Grades Management System

##  *Name*: CHINTHAPARTHI CHETHAN
## *Company*: CODTECH IT SOLUTIONS
## *ID*: CT6WDS1396
## *Domain*: PYTHON PROGRAMMING
## *Duration*: JULY to SEPTEMBER 2024
## *Mentor*: Neela Santhosh Kumar
### Overview of the Project
Project: Student Grades Management System
This Python project provides a simple management system for recording, calculating, and displaying student grades across various subjects. The system calculates the average grade, converts grades to a GPA scale, and determines the corresponding letter grade based on the GPA.

## Features
Add Grades: Allows users to add grades for different subjects.
Calculate Average Grade: Computes the average grade across all subjects.
Convert to GPA: Converts the numeric grade to a GPA (on a 10-point scale).
Determine Letter Grade: Determines the letter grade based on the GPA.
Display Summary: Displays a summary of all grades, the average grade, the average GPA, and the corresponding letter grade.
## Prerequisites
Python 3.x: Ensure that Python is installed on your system.
## Step-by-Step Guide to Using the System
Step 1: Running the Program
To run the Student Grades Management System, execute the student_grades.py file in your Python environment.

bash
Copy code
python student_grades.py
Step 2: Interacting with the Program
Upon running the program, you will be presented with a menu of options:

markdown
Copy code
Options:
1. Add a grade
2. Display summary
3. Exit
Add a Grade:

Select option 1 to add a grade.
You will be prompted to select a subject and enter a grade for that subject.
The grade should be between 0.0 and 100.0.
Display Summary:

Select option 2 to display a summary of all grades entered.
The summary will include the grades, corresponding GPA, average grade, average GPA, and letter grade.
Exit:

Select option 3 to exit the program.
Step 3: Example Interaction
Here's an example interaction with the program:

markdown
Copy code
Options:
1. Add a grade
2. Display summary
3. Exit
Enter your choice: 1
Subjects:
1. Math
2. Science
3. English
4. History
5. Physical Education
Select a subject by number: 1
Enter the grade for Math (0.0 - 100.0): 85.5

Options:
1. Add a grade
2. Display summary
3. Exit
Enter your choice: 2

Summary:
Math: Grade 85.5, GPA 8.55
Average Grade: 85.50
Average GPA: 8.55
Letter Grade: B
Code Overview
Class: StudentGrades
Attributes:

grades: A dictionary to store grades for each subject.
subjects: A list of available subjects.
## Methods:

add_grade(subject, grade): Adds a grade for the given subject.
calculate_average_grade(): Calculates the average grade across all subjects.
convert_to_gpa(grade): Converts a numeric grade to a GPA (out of 10).
get_letter_grade(gpa): Determines the letter grade based on the GPA.
display_grades(): Displays the grades and corresponding GPAs for each subject.
display_summary(): Displays a summary including average grade, GPA, and letter grade.
Main Function: main()
The main() function provides the user interface for interacting with the program. It handles the user's input, allows for adding grades, and displays a summary of the student's performance.
## Conclusion
This Student Grades Management System is a straightforward Python application designed to help manage and assess student performance across various subjects. It provides essential features for grade management, GPA conversion, and grade summarization.
