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
	if(betAmount == ""):
		if(vars.previousBet == None):
			return ("FormatError", 0)
		else:
			vars.gambleAmount = int(vars.previousBet)
			if currentMoney-int(vars.previousBet) < 0:
				return ("NotEnough",0)
			elif int(vars.previousBet) > 500:
				return ("TooMuch",0)
			else:
				return("Previous",int(vars.previousBet))
	if(betAmount.isdigit() == False or int(betAmount) <= 0):
		return ("FormatError", 0)
	else:
		betAmount = int(betAmount)
	if currentMoney-betAmount < 0:
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
def ShowSymbols(list_of_tuples, padding=5):

    reels = []

    for tup in list_of_tuples:
        reel_column = []
        for index in tup:
            symbol = vars.indexToSymbol[index]
            with open(f'AsciiArtSymbols/{symbol}.txt', 'r', encoding='utf-8') as f:
                lines = f.read().expandtabs(4).splitlines()

            max_width = max(len(line) for line in lines)
            lines = [line.ljust(max_width) for line in lines]

            reel_column.append(lines)  # store symbol lines

        reels.append(reel_column)


    for reel in reels:

        max_h = max(len(sym) for sym in reel)
        for sym in reel:
            width = len(sym[0])
            while len(sym) < max_h:
                sym.append(" " * width)

    # row 0: reels[0][0], reels[1][0], reels[2][0] ...
    # row 1: reels[0][1], reels[1][1], reels[2][1] ...
    # etc.

    num_rows = len(reels[0])  # number of symbols per column

    for row in range(num_rows):

        row_height = max(len(reels[col][row]) for col in range(len(reels)))

        for h in range(row_height):
            line_parts = []
            for col in range(len(reels)):
                line_parts.append(reels[col][row][h])
            print((" " * padding).join(line_parts))

        print()  # blank line between rows
