import random
import vars
def CreateRandomSeed():
	return random.randint(0,12345)


def GenerateNextXSlots(numberOfSlotsPerRow, numberOfRows):
	nextRows = []
	random.seed(vars.seed)
	for r in range(numberOfRows):
		row = []
		for s in range(numberOfSlotsPerRow):
			symbol = random.randrange(0, len(vars.indexToSymbol))
			row.append(symbol)
		nextRows.append(tuple(row))
	return nextRows

def BetCoins(betAmount, currentMoney):
	#FORMAT : (STATUS,MONEYTOPAY)
	if(betAmount.upper() == "LEAVE"):
		return ("LEAVE",0)
	if(betAmount.isdigit() == False or int(betAmount) <= 0):
		return ("FormatError", 0)
	else:
		betAmount = int(betAmount)
	if currentMoney-betAmount <= 0:
		return ("NotEnough",0)
	elif betAmount > 500:
		return ("TooMuch",0)
	else:
		return ("Success",betAmount)
	
def ConvertRawToSlots(rawList, numberOfLines=0):
	# take the first n tuples
	selected = rawList[0:numberOfLines]

	# convert values inside each tuple to symbols
	result = []
	for tup in selected:
		new_tup = tuple(vars.indexToSymbol[value] for value in tup)
		result.append(new_tup)

	return result

def ShowSymbols(listSymbols):
	for tuple in listSymbols:
		for index in tuple:
			symbol = vars.indexToSymbol[index]
			with open(f"AsciiArtSymbols/{symbol}.txt",'r', encoding = "utf-8") as f:
				print(f.read())
				if vars.indexToSymbol[0] == vars.indexToSymbol[1] == vars.indexToSymbol[2] == symbol:
					if symbol == "Bell":
						vars.money+= vars.symbolMultiplier[2]
						print("May the bells ring on your glory day! You have now: ", vars.money, "dollars!")
						input("press any key to try again: ")
					elif symbol == "Cherry":
						vars.money+= vars.gambleAmount*vars.symbolMultiplier[0]
						print("Cherries are always sweeter when they are in your favour! You have now:", vars.money, "dollars!")
						input("press any key to try again: ")
					elif symbol == "Lemon":
						vars.money+= vars.gambleAmount*vars.symbolMultiplier[1]
						print("Easy Peasy Lemon Squeezy! You have now:", vars.money,"dollars!")
						input("press any key to try again: ")
					elif symbol == "Clover":
						vars.money+= vars.gambleAmount*vars.symbolMultiplier[3]
						print("This is your lucky day!!! You have now:", vars.money,"dollars!")
						input("press any key to try again: ")
					elif symbol == 'Diamond':
						vars.money+= vars.gambleAmount*vars.symbolMultiplier[4]
						print("Shine on you crazy diamond!!! You have now:", vars.money,"dollars!")
						input("press any key to try again: ")
					elif symbol == 'Seven':
						vars.money+= vars.gambleAmount*vars.symbolMultiplier[4]
						print("I don't understand how a single number can make you so rich... You have now:", vars.money,"dollars!")
						input("press any key to try again: ")
				else:
					print('Dang it...')
					vars.money-= vars.gambleAmount
					print("You have now: ",vars.money, "dollars")
					input("press any key to try again: ")


					

ShowSymbols()











	