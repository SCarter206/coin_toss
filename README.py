import random
bank = 100
#reminds user of choice they made, 0heads or 1tails
class coin_proccess():
    def user_coin_choice(recieve_user_coin_input):
        if recieve_user_coin_input == 0:
            print("you chose heads")
            return "heads"
        elif recieve_user_coin_input == 1:
            print("you chose tails")
            return "tails"
        else:
            return "just type 0 or 1 and press enter"
#computer chooses 0heads or 1tails at random
class comp_coin_flip():
    def coin_flip(list):
        list = [0, 1]
        random.choice(list)
        if x == 0:
            return("heads")
        elif x == 1:
            return("tails")
#asks and stores users input 0heads or 1tails
class recieve_user_coin_input():
        def user_coin_input(y):
            y = eval(input("0 for heads and 1 for tails\n"))
            return y
#asks and stores users bet
class recieve_user_bet_input():
    def get_user_bet(z):
        z = eval(input("how much would you like to bet\n"))
        return z
#compares users coin choice and computers coin choice
class compare_coin_results():
    def compare(comp_coin_flip, recieve_user_coin_input):
        if comp_coin_flip == recieve_user_coin_input:
            return "you won"
        else:
            return "sorry try again"
#adds to or subtracts from bet amount and stores for next round
class bank_effects():
    bank = 100
    def user_bank(compare_coin_results, bank):
        if compare_coin_results() == "you won":
            return "you now have " + bank + z
        else:
            return "you now have " + bank - z

def main():
    print("Welcome to heads or tails. You'll start your bank with $100")

    obj = recieve_user_coin_input()
    obj.user_coin_input()

    obj = recieve_user_bet_input()
    obj.get_user_bet()

    obj = coin_proccess()
    obj.user_coin_choice()

    obj = comp_coin_flip()
    obj.coin_flip(list)

    obj = compare_coin_results()
    obj.compare(comp_coin_flip, recieve_user_coin_input)

    obj = bank_effects()
    obj.user_bank(compare_coin_resluts, bank)

if __name__ == "__main__":
    main()
