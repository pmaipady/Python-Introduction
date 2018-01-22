from random import randint
print ("Problem 2: Guess my number")
random_num = randint(0, 10)
print ("the random number is: ", random_num)
guess = int (input("Please enter a number between 0 and 10: "))
while (guess<=random_num):
  if guess < random_num:
    guess = int(input("The number is greater. Please guess again: "))
  elif guess > random_num:
    guess = int(input("The number is lower. Please guess again: "))

print ("That's the correct number. Congrats! \n")
