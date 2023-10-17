users = [
    (0, "Lee","password"),
    (1,"Rolf", "lee123"),
    (2, "Jose", "longpass1234"),
    (3, "username", "1234"),
]

#Create a mappy of usernames to information

username_mapping = {user[1]: user for user in users}

print(username_mapping["Lee"]) # wold get back the entire results of Lee's Tuple

username_input = input("Enter username: ")
password_input = input("Enter password: ")

_, username, password = username_mapping[username_input]

if password_input == password:
    print("Correct details!")
else:
    print("Incorrect details :(")