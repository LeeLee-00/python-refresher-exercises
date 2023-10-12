name = input("Enter your name please: ")
print(name)

#Doing wit with math
size_input = input("Your house size in sqaure feet: ")
sqaure_feet = int(size_input) 
sqaure_metres = sqaure_feet / 10.8
print(f"Okay Mr {name} your {sqaure_feet} sqaure feet is {sqaure_metres:.2f} sqaure metres")