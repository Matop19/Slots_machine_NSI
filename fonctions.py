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
def ShowSymbolTuple(_tuple, padding=5):

	allSymbolsLines = []
	for index in _tuple:
		try:
			symbol = vars.indexToSymbol[index]
			with open(f'AsciiArtSymbols/{symbol}.txt', 'r', encoding='utf-8') as f:
				lines = f.read().splitlines()
				allSymbolsLines.append(lines)
		except FileNotFoundError:
			print(f"⚠️ Missing ASCII file for symbol: AsciiArtSymbols/{symbol}.txt")
			return

	# Equalize heights (so cards align properly)
	max_height = max(len(c) for c in allSymbolsLines)
	for c in allSymbolsLines:
		while len(c) < max_height:
			c.append(" " * len(c[0]))

    # Print cards side by side
	for line_group in zip(*allSymbolsLines):
		print((" " * padding).join(line_group))
				
def ShowSymbols(symbolsList, padding=5):
	for _tuple in symbolsList:
		ShowSymbolTuple(_tuple, padding)

ShowSymbols([(0,1,2),(3,4,5)])







	