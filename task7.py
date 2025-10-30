def analyze_student_grades():
    # Sample data
    student_names = ["Alice", "Bob", "Charlie", "Diana"]
    student_grades = [85, 92, 78, 90]

    # 1. Print a welcome message
    print("Welcome to the Student Grades Analyzer!\n")

    # 2. Determine and print the number of students
    num_students = len(student_names)
    print("Number of students:", num_students)

    # 3. Print the type of the student names list and the grades list
    print("\nType of student_names list:", type(student_names))
    print("Type of student_grades list:", type(student_grades))

    # 4. Find and print the highest and lowest grade
    highest_grade = max(student_grades)
    lowest_grade = min(student_grades)
    print("\nHighest grade:", highest_grade)
    print("Lowest grade:", lowest_grade)

    # 5. Print the list of grades sorted in ascending order
    sorted_grades = sorted(student_grades)
    print("\nSorted grades:", sorted_grades)

    # 6. Print the list of grades in reverse order
    reversed_grades = list(reversed(sorted_grades))
    print("Reversed grades:", reversed_grades)

    # 7. Generate and print a range of grade indices from 1 to the number of students
    grade_indices = list(range(1, num_students + 1))
    print("\nGrade indices from 1 to number of students:", grade_indices)

# Run the analysis
analyze_student_grades()





def add(a, b):
    """Return the sum of two numbers."""
    return a + b
def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b
def multiply(a, b):
    """Return the product of two numbers."""
    return a * b
def divide(a, b):
    """Return the quotient of two numbers. Handles division by zero."""
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
def greet(name):
    """Return a greeting message for the user."""
    return f"Hello, {name}! Welcome to the program."
def main():
    # Demonstrating the use of user-defined functions
    # Arithmetic operations
    num1 = 10
    num2 = 5
    print("Arithmetic Operations:")
    print(f"Sum of {num1} and {num2}:", add(num1, num2))
    print(f"Difference between {num1} and {num2}:", subtract(num1, num2))
    print(f"Product of {num1} and {num2}:", multiply(num1, num2))
    print(f"Quotient of {num1} and {num2}:", divide(num1, num2)
    # Greeting the user
    user_name = "Alice"
    print("\nGreeting:")
    print(greet(user_name))

# Run the main function
if __name__ == "__main__":
    main()




