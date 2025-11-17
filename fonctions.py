import random
import vars
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
	print(rawList)
	#LIST IN FORMAT [(1,2,...), ...]
	# take the first n tuples
	selected = rawList[:numberOfLines]

	# flatten them into a single list
	result = []
	for tup in selected:        # first loop: each tuple
		for value in tup:       # second loop: each value in the tuple
			result.append(value)

	symbols = []
	for index in result:
		symbols.append(vars.indexToSymbol[index])
	return symbols
