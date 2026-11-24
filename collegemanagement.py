student_name = input("Enter student name: ")
usn = input("Enter USN: ")
course = input("Enter course name: ")
semester = int(input("Enter semester: "))
department = input("Enter department: ")
phone_number = input("Enter phone number: ")
email = input("Enter email: ")
subject1 = int(input("Enter subject 1 marks: "))
subject2 = int(input("Enter subject 2 marks: "))
subject3 = int(input("Enter subject 3 marks: "))
attendance = float(input("Enter attendance percentage: "))

total = subject1 + subject2 + subject3
percentage = total / 3

if percentage >= 35:
    result = "Pass"
else:
    result = "Fail"

print("\n--- College Management System ---")
print("Student Name:", student_name)
print("USN:", usn)
print("Course:", course)
print("Semester:", semester)
print("Department:", department)
print("Phone Number:", phone_number)
print("Email:", email)
print("Subject 1 Marks:", subject1)
print("Subject 2 Marks:", subject2)
print("Subject 3 Marks:", subject3)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Attendance:", attendance, "%")
print("Result:", result)

with open("students.txt", "a") as f:
    f.write(f"{student_name}, {usn}, {course}, {semester}, "
            f"{department}, {phone_number}, {email}, "
            f"{total}, {percentage}, {attendance}, {result}\n")

print("\nStudent details saved successfully!")