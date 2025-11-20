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
def ShowSymbols(list_of_tuples, padding=5):
    # list_of_tuples is like: [(1,2,3), (4,5,6), (7,8,9)]
    
    # Load all ASCII arts into a structure:
    # reels[i][j] = ASCII art (list of lines) for tuple i, symbol j
    reels = []

    for tup in list_of_tuples:
        reel_column = []
        for index in tup:
            symbol = vars.indexToSymbol[index]
            with open(f'AsciiArtSymbols/{symbol}.txt', 'r', encoding='utf-8') as f:
                lines = f.read().expandtabs(4).splitlines()

            # Normalize width inside the symbol
            max_width = max(len(line) for line in lines)
            lines = [line.ljust(max_width) for line in lines]

            reel_column.append(lines)  # store symbol lines

        reels.append(reel_column)

    # Each symbol has its own height; normalize all heights in each reel
    for reel in reels:
        # find maximum height among symbols in this reel
        max_h = max(len(sym) for sym in reel)
        for sym in reel:
            width = len(sym[0])
            while len(sym) < max_h:
                sym.append(" " * width)

    # Now print row by row:
    # row 0: reels[0][0], reels[1][0], reels[2][0] ...
    # row 1: reels[0][1], reels[1][1], reels[2][1] ...
    # etc.

    num_rows = len(reels[0])  # number of symbols per column

    for row in range(num_rows):
        # find max height of this row across all reels
        row_height = max(len(reels[col][row]) for col in range(len(reels)))

        # print this row line by line
        for h in range(row_height):
            line_parts = []
            for col in range(len(reels)):
                line_parts.append(reels[col][row][h])
            print((" " * padding).join(line_parts))

        print()  # blank line between rows
