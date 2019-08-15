#project in python 3
#program name: coin toss with gamble

import random

#recives users choice of heads or tails using 0 and 1
#compares and returns true of false
def coin_matter():
    user_choice = input("Input 0 for heads or 1 for tails: ")
    list = [0, 1]
    result = random.choice(list)
    if int(user_choice) == int(result):
        return True
    else:
        return False

#recieves users bet amount
def bet_amount():
    y = input("how much would you like to bet: ")
    return y

#verifies that the user is not betting more then they have
def bet_vs_bank(bank_amount):
    bet = bet_amount()
    if int(bet) > bank_amount:
        print("you cant bet more then you have, try again")
        return bet_vs_bank(bank_amount)
    else:
        return bet


#loops until bank amount reaches zero
def bank():
    bank_amount = 100
    while bank_amount > 0:
        bet_amount = int(bet_vs_bank(bank_amount))
        coin_result = coin_matter()
        if coin_result == True and bank_amount > 0:
            print("you won and now have")
            bank_amount += bet_amount
            print(bank_amount)
        elif coin_result == False and bank_amount > 0:
            print("you lost and now have")
            bank_amount -= bet_amount
            print(bank_amount)
    else:
        return "Have a shot at try again"

print("The game is heads or tails. Match the computers random choice.")
print("You will start with 100 in the bank. ")
print(bank())

