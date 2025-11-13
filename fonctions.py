import random
import vars
def GenerateNextXSlots(numberOfSlotsPerRow, numberOfRows):
	nextRows = []
	random.seed(vars.seed)
	for r in range(numberOfRows):
		row = []
		for s in range(numberOfSlotsPerRow):
			symbol = random.randrange(0, 6)
			row.append(symbol)
		nextRows.append(tuple(row))
	return nextRows



if __name__ == "__main__":
	nextTenSlots = GenerateNextXSlots(5, 5)
	print(nextTenSlots)