a = []
b = a

print(id(a))
print(id(b))

a.append(35)

print(a)
print(b)