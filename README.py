# coin_toss
#heads or tails project in python 3
#im getting a positional error code:
"""
Welcome to heads or tails. You'll start your bank with $100
0 for heads and 1 for tails
1
you chose tails
how much would you like to bet
1
Traceback (most recent call last):
  File "coin_toss.py", line 53, in <module>
    main()
  File "coin_toss.py", line 48, in main
    obj.compare()
TypeError: compare() missing 1 required positional argument: 'user_coin_choice'
"""
# ive google searched the rules on positional arguments but im not finding literature regarding the whole file. Any advice appreciated.
# just a beginner

import random
bank = 100

class coin_proccess():
    def user_coin_choice(y):
        y = eval(input("0 for heads and 1 for tails\n"))
        if y == 0:
            print("you chose heads")
            return "heads"
        elif y == 1:
            print("you chose tails")
            return "tails"
        else:
            return "just type 0 or 1 and press enter"

    def get_user_bet(z):
        z = eval(input("how much would you like to bet\n"))
        return z

    def coin_flip(list, x):
        list = [0, 1]
        x = random.choice(list)
        if x == 0:
            return("heads")
        elif x == 1:
            return("tails")

    def compare(coin_flip, user_coin_choice):
        if coin_flip() == user_coin_choice():
            return "you won"
        else:
            return "sorry try again"

    def user_bank(compare):
        if compare() == "you won":
            return "you now have " + bank + z
        else:
            return "you now have " + bank - z


def main():
    print("Welcome to heads or tails. You'll start your bank with $100")

    obj = coin_proccess()
    obj.user_coin_choice()
    obj.get_user_bet()
    obj.coin_flip('x')
    obj.compare()
    obj.user_bank()


if __name__ == "__main__":
    main()

