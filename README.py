import random
#improved argument positions, clearer notes, initialized variables(bank, y), user_bank wont add or subtract just provides uneffected bank value
class coin_proccess():
    bank = 0
    y = 0
#recieves user input, heads or tails using 0 and 1
    def user_coin_choice(x):
        y = eval(input("0 for heads and 1 for tails\n"))
        if y == 0:
            print("you chose heads")
            return 'heads'
        elif y == 1:
            print("you chose tails")
            return 'tails'
        else:
            return "just type 0 or 1 and press enter"
#recieves amount user wants to bet
    def user_bet(y):
        y = eval(input("how much would you like to bet\n"))
        return y
#computer randomly selects heads or tails and notifies user
    def coin_flip(z):
        list = [0, 1]
        z = random.choice(list)
        if z == 0:
            print("coin has landed on heads")
            return 'heads'
        elif z == 1:
            print("coin has landed on tails")
            return 'tails'
#compares users input and comp. random choice
    def compare(coin_flip, user_coin_choice):
        if coin_flip == user_coin_choice:
            return "you won"
        else:
            return "sorry try again"
#takes user bet amount provided earlier and adds or subtracts from bank
    def user_bank(compare, bank, y):
        bank = 100
        y = int()
        if compare == "you won":
            print("you won and now have a score of " + str(bank + y))

        else:
            print("you lost and now have a score of " + str(bank - y))


def main():

    print("Welcome to heads or tails. You will start with $100")
    obj = coin_proccess()
    obj.user_coin_choice()
    obj.user_bet()
    obj.coin_flip()
    obj.compare('user_coin_choice')
    obj.user_bank('compare', 'y')

if __name__ == "__main__":
        main()
