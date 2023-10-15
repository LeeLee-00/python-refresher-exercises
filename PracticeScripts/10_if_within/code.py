movies_watched = {"The Matrix", "Power Rangers", "Get Out"}
user_movie = input("Enter movie you recenetly watched: ")

if user_movie in movies_watched:
    print(f"I've watched {user_movie} too!")
else:
    print("I haven't watched that yet.")
    

### Magic Number

number = 7

user_input = input("Enter 'y' if you want to play: ")

if user_input in ("y", "Y"):
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) in (1,-1):
        print("You were off by one.")
    else:
        print(f"Sorry, its wrong. You the number was {number}. Good Bye!")