## The while loop

number = 7

while True:
    user_input = input("Would you like to play? (Y/n): ")

    if user_input == "n":
        break

    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) in (1,-1):
        print("You were off by one.")
    else:
        print(f"Sorry, its wrong. You the number was {number}. Good Bye!")

## For loop to generate friends
friends = ["Lee", "John", "Brandon", "Bradd"]

for friend in friends:
    print(f"{friend} is my friend. :)")

#fOR LOOP TO CALCUALTE GRADES

print("\n")

grades = [40, 25, 60, 100, 99]
total = 0
amount = len(grades)

for grade in grades:
    total += grade

print(total/amount)