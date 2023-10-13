local = {"Lee"}
abroad = {"Bob","Greg"}

local_friends = abroad.difference(abroad)
#print(local_friends)

friends = local.union(abroad)
#print(friends)

humanities = {"Bob", "Leland","Victor","Lee"}
engineering = {"Lee","Manuel","Dereck","Victor"}

school = humanities.intersection(engineering)
print(school)


print("Practicing Set Operations continued.")

set_1 = {1,2,3,4,5,6,7}
set_2 = {4,5,6,7,8,9,2}

print("\n")

print('Combine set_1 and set_2')
print(set_1.union(set_2))  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

print("\n")

print('Finding common elements in set_1 and set_2')
print(set_1.intersection(set_2)) # {2, 4, 5, 6, 7}

print("\n")
print("Now using spcial set operators")
print("\n")

print("Now Combining set_1 and set_2")
print(set_1 | set_2) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

print("\n")

print("Finding common elements in set_1 and set_2")
print(set_1 & set_2) # {2, 4, 5, 6, 7}

print("\n")

print("Find elements in set_1 that are not in set_2")
print(set_1 - set_2) # {1, 3}

print("\n")

# Chaining together 3 sets
set_3 = {5, 6, 7, 8, 9, 100}

print(set_1 | set_2 | set_3) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 100}