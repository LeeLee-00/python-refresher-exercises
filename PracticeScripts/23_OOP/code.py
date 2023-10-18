class Student: #Def of something this thing will have a name of Rolf
    def __init__(self, name, grades): #init is a method due to a functoin being in a class.
        self.name = name #Object is "Self" - the Property is "name"
        self.grades = grades
    
    def average_grades(self):
        return sum(self.grades) / len(self.grades)

student = Student("Lee", (90,100,100,65,40,90))
student2 = Student("Greg", (100,100,100,25,20,20))
print(student.name)
print(student.average_grades())

print(student2.name)
print(student2.average_grades())
#define methods ion a class that used the object within the method to use thm.