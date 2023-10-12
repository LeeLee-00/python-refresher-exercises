l = ["Lee", "John", "Adam"] #Keep sames orders
t = ("Lee", "John", "Adam") #can't modify tuples
s = {"Lee", "John", "Adam"} #can't duplicate elements in a set and order is not gaurenteed

print(t[0]) #gets elements in 0 which is me Lee!

l.append("Smith")

print(l)


l.remove("John")
print(l)

#Information - Ntice that its add, and not append, whjen working with sets. 
# Because append means "add a the end" 
# But sets don't ahve an end since they don't have order

s.add("Smith")
print(s)

# List is the most standarad collection
# Tuple is not modifiable
# Set has no duplicate and no order.