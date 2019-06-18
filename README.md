# coin_toss
heads or tails project
# this does not seem to consistantly work. almost seems to randomly select true or false as well.


import random
list = "heads", "tails"
def coin_flip(heads_tails):
	print(random.choice(list))
	if random.choice(list) == heads_tails:
		return True
	else:
		return False
		
print(coin_flip("heads"))

