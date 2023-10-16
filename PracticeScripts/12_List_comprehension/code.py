numbers = [1,3,5]
doubled = [num * 2 for num in numbers]

#Friends list comprehension

friends = ["Rolf", "Sam", "Sammy","Lee", "Saurahb"]
starts_s = [friend for friend in friends if friend.startswith("S")]


print(friends)
print(starts_s)
print(friends is starts_s)
print("friends: ", id(friends), "starts_s:", id(starts_s))