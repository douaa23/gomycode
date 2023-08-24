import numpy as np

def calculate_grade(percentage):
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B+'
    elif percentage >= 60:
        return 'B'
    elif percentage >= 50:
        return 'C'
    else:
        return 'F'

def main():
    num_students = int(input("Enter the number of students: "))
    num_subjects = int(input("Enter the number of subjects: "))
    
    student_names = []
    marks = np.empty((num_students, num_subjects))
    
    for i in range(num_students):
        name = input(f"Enter the name of student {i + 1}: ")
        student_names.append(name)
        print(f"Enter marks for student {name}:")
        for j in range(num_subjects):
            mark = float(input(f"Enter marks for subject {j + 1} for {name}: "))
            marks[i, j] = mark
    
    total_marks = np.sum(marks, axis=1)
    percentages = (total_marks / (num_subjects * 100)) * 100
    
    print("\nResult:")
    print("--------------------------------------------------------")
    print("Student\tTotal Marks\tPercentage\tGrade")
    print("--------------------------------------------------------")
    
    for i in range(num_students):
        grade = calculate_grade(percentages[i])
        print(f"{student_names[i]}\t{total_marks[i]}\t\t{percentages[i]:.2f}%\t\t{grade}")
    
    print("--------------------------------------------------------")

if __name__ == "__main__":
    main()
