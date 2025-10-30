# Initialize the list of grades
grades = [85, 90, 78, 92, 88]

# Display the grades list
print("Grades List:", grades)

# Prompt the user to enter the index of the grade they want to view
try:
    index = int(input("Enter the index of the grade you want to view: "))
    # Attempt to display the grade at the specified index
    print(f"The grade at index {index} is: {grades[index]}")
except IndexError:
    # Handle the case where the index is out of range
    print("Invalid index. Please enter a valid index.")
except ValueError:
    # Handle the case where the input is not an integer
    print("Invalid input. Please enter a numerical index.")



# Function to perform division
def divide_numbers():
    try:
        # Prompt the user to enter the numerator
        numerator = float(input("Enter the numerator: "))
        # Prompt the user to enter the denominator
        denominator = float(input("Enter the denominator: "))
        # Attempt to perform division
        result = numerator / denominator
        print(f"Result: {result}")
    except ZeroDivisionError:
        # Handle division by zero error
        print("Error: Division by zero is not allowed.")
    except ValueError:
        # Handle invalid input that is not a number
        print("Error: Please enter valid numbers.")

# Call the function to execute the division operation
divide_numbers()




# define Python user-defined exceptions
class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    pass
# you need to guess this number
number = 18

try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")

except InvalidAgeException:
    print("Exception occurred: Invalid Age")

