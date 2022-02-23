#Create a student class (name the file StudentClass.py). 
#The class  should have 4 attributes. StudentID, Name, 
#DOB and classification  (F,S,Jr,Sr).
class StudentClass:

    def __init__(self,StudentID,StudentName,DOB,Classification):
        self.__StudentID = StudentID
        self.__StudentName = StudentName
        self.__DOB = DOB
        self.__Classification = Classification

#Create a method that will calculate the 
#student’s current age (accessor)

#Create a method that will determine when 
#the student can  register (accessor)

#Create a method to return the age and another 
#method to return the registration dates. (accessor)