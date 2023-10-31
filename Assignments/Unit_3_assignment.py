# Initialize variables as needed
numGrades = 0
totalGrades = 0
# Prompt user to input number of greades to be processed. Store this value in a variable (numGrades)
numGrades = int(input("Enter number of grades to process: "))

# Prompt the user to enter a student name and store in a variable
studentName = input("Enter student name: ")

# Create a conditional loop and cont. processing grade values until given number is reached
gradeCount = 0

while gradeCount < numGrades:
    try:
        grade = float(input(f"Enter grade {gradeCount + 1}: "))
        totalGrades += grade
        gradeCount += 1
    except ValueError:
        print("Invalid inpuit. Please entere a numeric grade.")

# Calculate the student's average
studentAverage = totalGrades / numGrades

# Display the naem of the student and their average
print(f"Student: {studentName}")
print(f"Average Grade: {studentAverage}")