import random

money = 100

#Write your game of chance functions here

def coinToss(guess, bet):
  print("Let's play Coin toss!")

  if (bet <= 0):
        print("You need to bet more than 0 to play.")
        return 0

  num = random.randint(1, 2)
  if (num == 1):
    print("Heads")
  else:
    print("Tails")

  if (guess == num):
    print("You won!")
    newMoney = money + bet
    print("You now have " + str(newMoney) + " in your account.")
    return newMoney
  else:
    print("You lost.")
    newMoney = money - bet
    print("You now have " + str(newMoney) + " in your account.")
    return newMoney

def choHan(guess, bet):
  print("Let's play ChoHan!")

  if (bet <= 0):
        print("You need to bet more than 0 to play.")
        return 0

  dice1 = random.randint(1, 6)
  dice2 = random.randint(1, 6)
  
  diceTotal = dice1 + dice2

  if (diceTotal == 1,3,5,7,9,11):
    print("Odd")
  else:
    print("Even")

  if (guess == diceTotal):
    print("You won!")
    newMoney = money + bet
    print("You now have " + str(newMoney) + " in your account.")
    return newMoney
  else:
    print("You lost.")
    newMoney = money - bet
    print("You now have " + str(newMoney) + " in your account.")
    return newMoney

def randomCard(bet):
    print("Let's play 'Who's card is higher?'")

    if (bet <= 0):
        print("You need to bet more than 0 to play.")
        return 0

    card1 = random.randint(1, 13)
    card2 = random.randint(1, 13)
    print("You drew this card: " + str(card1))
    print("They drew this card: " + str(card2))

    if (card1 > card2):
        print("You won!")
        newMoney = money + bet
        print("You now have " + str(newMoney) + " in your account.")
        return newMoney

    elif (card1 < card2):
        print("You lost.")
        newMoney = money - bet
        print("You now have " + str(newMoney) + " in your account.")
        return newMoney

    else:
        print("Tie!")
        newMoney = money
        return newMoney

def roulette(guess, bet):
  print("Let's play Roulette!")

  if (bet <= 0):
        print("You need to bet more than 0 to play.")
        return 0

  num = random.randint(0, 37)

  if (num == 37):
    print("00")

  elif (num == 1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35):
    print("Odd")

  else:
    print("Even")

  if (guess == "Even" and num != 0):
    print("You won!")
    newMoney = money + bet
    print("You now have " + str(newMoney) + " in your account.")
    return newMoney

  elif (guess == "Odd" and num != 37):
    print("You won!.")
    newMoney = money + bet
    print("You now have " + str(newMoney) + " in your account.")
    return newMoney

  elif (guess == num):
    print("You won!")
    newMoney = money + (bet * 35)
    print("You now have " + str(newMoney) + " in your account.")
    return newMoney

  else:
    print("You lost")
    newMoney = money - bet
    print("You now have " + str(newMoney) + " in your account.")
    return newMoney

#Call your game of chance functions here

money = coinToss(2, 15) + choHan(7, 20) + randomCard(10) + roulette(18,30)


