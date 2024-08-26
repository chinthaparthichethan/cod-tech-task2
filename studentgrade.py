class StudentGrades:
    def __init__(self):
        self.grades = {}
        self.subjects = ['Math', 'Science', 'English', 'History', 'Physical Education']

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def calculate_average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def convert_to_gpa(self, grade):
        return grade / 10

    def get_letter_grade(self, gpa):
        if gpa >= 9.0:
            return 'A'
        elif gpa >= 8.0:
            return 'B'
        elif gpa >= 7.0:
            return 'C'
        elif gpa >= 6.0:
            return 'D'
        else:
            return 'F'

    def display_grades(self):
        for subject, grade in self.grades.items():
            gpa = self.convert_to_gpa(grade)
            print(f"{subject}: Grade {grade}, GPA {gpa:.2f}")

    def display_summary(self):
        average_grade = self.calculate_average_grade()
        average_gpa = self.convert_to_gpa(average_grade)
        letter_grade = self.get_letter_grade(average_gpa)
        
        print("\nSummary:")
        self.display_grades()
        print(f"Average Grade: {average_grade:.2f}")
        print(f"Average GPA: {average_gpa:.2f}")
        print(f"Letter Grade: {letter_grade}")

def main():
    student = StudentGrades()
    
    while True:
        print("\nOptions:")
        print("1. Add a grade")
        print("2. Display summary")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("Subjects:")
            for i, subject in enumerate(student.subjects, start=1):
                print(f"{i}. {subject}")
            subject_choice = int(input("Select a subject by number: "))
            if 1 <= subject_choice <= len(student.subjects):
                subject = student.subjects[subject_choice - 1]
                grade = float(input(f"Enter the grade for {subject} (0.0 - 100.0): "))
                if 0.0 <= grade <= 100.0:
                    student.add_grade(subject, grade)
                else:
                    print("Invalid grade. Please enter a value between 0.0 and 100.0.")
            else:
                print("Invalid subject choice. Please try again.")
        elif choice == '2':
            student.display_summary()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
