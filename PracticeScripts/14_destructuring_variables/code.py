#Destructuring variables: 
# assigning a data structuring to two vairables and splitting its components

t = 5,11

x,y = t
print(x,y)

# List dictiionaries continued 
student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

#Trning into list becuase .items() doesn't returna  lsit of tuples.

print(list(student_attendance.items()))

for t in student_attendance.items():
    print(t)