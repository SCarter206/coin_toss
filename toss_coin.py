import random


#intro meant to be used once
def intro():
    print("----Welcome to heads or tails. \nPlease use 0 for heads and 1 for tails \nbut first...")
#user input and compare to comp. results
def betta_work():
    x = input("----Please select heads(0) or tails(1):")
    list = [0,1]
    y = random.choice(list)
    if x == y:
        return 0
    else:
        return 1
#user input bet amount
def bet():
    bank = 100
    while bank > 0:
        bet = int(input("What would you like to bet?(0-100):"))
        if betta_work() == 0:
            bank += bet
            print('You won and now have %s!') % (bank)
        else:
           bank -= bet
           print('You lost and now have %s!') % (bank)
        
#meant to loop program

def main():
    intro()
    bet()
#still need to store variable across loop
main()
#things to consider for next time: what if i want to bet a negative number?
# what if a user bets a string and not a number?
# what if a user enters an integer that looks like this: 00990 for a bet?
# error handling, what if a user enters nothing at all?
