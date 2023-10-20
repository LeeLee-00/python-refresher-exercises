def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element within {expected}.")

friends = [
    {"name": "LeeLee", "age":24},
    {"name": "Dawn", "age":33},
    {"name": "Charly", "age":40},
]

def get_friend_name(friend):
    return friend["name"]

print(search(friends, "LeeLee", lambda friend: friend["name"]))