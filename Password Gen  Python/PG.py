import random

print("Please capitalise first alphabet of your names")
Name = input("Enter your name: ")
Surname = input("Enter Your Surname: ")

Letters = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
Characters = "0123456789_!*&$%@?<>."

EntryPassword = " "

y = input('please type "generate" to generate your temporal password: ', '\n' )


if y == "generate":
      for i in range(16):
          x = random.randint(1,2)

          if x == 1:
               EntryPassword += Letters[random.randint(0,25)]
          else:
               EntryPassword += Characters[random.randint(0,20)]

print("Your Login Details are as follows:: ", '\n')
print(Name.capitalize())
print(Surname.capitalize())
print("YOUR GENERATED PASSWORD IS: " , EntryPassword)

