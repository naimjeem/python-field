import random

theNum = random.randint(1, 20)

print('Guess a number between 1 and 20')

for guessTaken in range(1, 7):
  print('Guess a number')
  guess = int(input())

  if guess < theNum:
    print('Your guess is too low')
  elif guess > theNum:
    print('Your guess is too high')
  else:
    break

if guess == theNum:
  print('Good job! You guessed my number in ' + str(guessTaken) + ' guesses!')
else:
  print('Nope. The number I was thinking of was ' + str(theNum))