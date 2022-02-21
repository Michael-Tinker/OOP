#Create a program file (name the file StudentProgram.py) that will
#create an instance of the student class and display the age of the
#student and when they can register.

import StudentClass as stud

def main():
    # Get the starting inputs
   StudentID = int(input('Enter the student ID: '))
   StudentName = input("Enter the student name: ")
   print("Student Date of Birth")
   DOB_day = int(input("Enter the Day: "))
   DOB_month = int(input("Enter the Month: "))
   DOB_year = int(input("Enter the Year: "))
   Classification = input("Enter the classification (F,S,Jr,Sr): ")

   # Create a Student object.
   student = stud.StudentClass(StudentID, StudentName, DOB_day, DOB_month, DOB_year, Classification)

   # Display the students's details according to the class
   print("StudentID: ", student.get_StudentID())
   print("Name: ", student.get_StudentName())
   print("DOB: ", student.get_DOB())
   print("Classification: ", student.get_Classification())
      
 
main()