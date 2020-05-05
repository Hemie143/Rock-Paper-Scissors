# Write your code here
import random

#
name = input("Enter your name:")
print(f'Hello, {name}')
rating = 0

ratings = open("rating.txt")
for line in ratings:
    user, points = line.split()
    if user == name:
        rating = int(points)
        break
ratings.close()

options = input()
if options:
    options = options.split(',')
else:
    options = ["rock", "paper", "scissors"]
options_num = len(options)

print("Okay, let's start")
while True:
    user = input()
    if user == "!exit":
        print("Bye!")
        break
    elif user == "!rating":
        print(f'Your rating: {rating}')
        continue
    elif user not in options:
        print("Invalid input")
        continue
    user_index = options.index(user)
    others = options[user_index+1:] + options[:user_index]
    computer = random.choice(options)
    score = 0
    if computer == user:
        print(f'There is a draw ({computer})')
        score = 50
    else:
        computer_index = others.index(computer)
        if computer_index < options_num // 2:
            print(f'Sorry, but computer chose {computer}')
        elif computer_index > options_num // 2:
            print(f'Well done. Computer chose {computer} and failed')
            score = 100
    rating += score