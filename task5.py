def find_employee_by_id(employees, target_id):
    for employee in employees:
        if employee['id'] == target_id:
            return employee
    return None

# Test the function
employees = [
    {'id': 1, 'name': 'Alice', 'department': 'HR'},
    {'id': 2, 'name': 'Bob', 'department': 'Engineering'},
    {'id': 3, 'name': 'Charlie', 'department': 'Sales'},
]
print(find_employee_by_id(employees, 2))  # Output: {'id': 2, 'name': 'Bob', 'department': 'Engineering'}



def bubble_sort_scores(students):
    n = len(students)
    for i in range(n):
        # Track if any swap is made in this pass
        swapped = False
        for j in range(0, n-i-1):
            if students[j]['score'] > students[j+1]['score']:
                # Swap if the score of the current student is greater than the next
                students[j], students[j+1] = students[j+1], students[j]
                swapped = True
        # If no two elements were swapped, the list is already sorted
        if not swapped:
            break
# Example usage
students = [
    {'name': 'Alice', 'score': 88},
    {'name': 'Bob', 'score': 95},
    {'name': 'Charlie', 'score': 75},
    {'name': 'Diana', 'score': 85}
]
print("Before sorting:")
for student in students:
    print(student)
bubble_sort_scores(students)
print("\nAfter sorting:")
for student in students:
    print(student)
