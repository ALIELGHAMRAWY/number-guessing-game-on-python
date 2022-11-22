import random
comGuess=random.randint(0,100)

while True:
  userGuess=int(input("guess a number between 0-100:"))
  if userGuess>comGuess:
      print("guess lower")
  elif userGuess<comGuess:
          print("guess higher")
  else:
              print("congratulation")
              break
