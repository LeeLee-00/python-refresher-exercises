import datetime #Messsing around with importing a library.


name = 'Lee'
#f string - embed variables inside srtings


print (f"Hello, {name}")

name = 'Roplf'

print (f"Hello, {name}")


#Template strings with .format()
name = "Lee"
greeting = "Hello, {}"
with_name = greeting.format(name)

print(with_name)

#Longer phrases

today = datetime.datetime.now()

longer_phrase = "Hello, {}, Today is {} {}"

formatted = longer_phrase.format("Lee", today.strftime("%B"), today.strftime("%d"))
print(formatted)


