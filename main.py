#FICHIER MAIN OU LE JEU SE DEROULE :)
from fonctions import *
import os
from time import sleep
#region SYNC TO MAIN
#endregion
def NewGame():
	os.system('cls' if os.name == 'nt' else 'clear')
	#region GAMBLE
	betCoins = ("None",0)
	while betCoins[0]!="Success":
		gambleAmount = input(f'''Entrez la quantité d'$ que vous souhaitez parier\nYou currently have ${vars.money}\nQuittez en entrant "LEAVE"''')
		betCoins = BetCoins(gambleAmount, vars.money)

		match betCoins[0]:
			case "FormatError":
				print("The format of the bet is incorrect !")
			case "NotEnough":
				print("You do not have enough money !")
			case "TooMuch":
				print("Your bet amount exceeds the upper limit !")
			case "LEAVE":
				print("You decide to leave.")
				exit()
	vars.money -= betCoins[1]
	vars.gambleAmount = int(gambleAmount)
	print(f"You gambled {vars.gambleAmount}, and now have {vars.money}")
	sleep(1)
	#endregion

	#region Slot Logic
	vars.seed = CreateRandomSeed()
	print("Seed",vars.seed)
	vars.nextSlotsRow = GenerateNextXSlots(3,3)
	#A REMPLACER
	vars.numberOfBoughtRows = int(input("Cmb de lignes ?(max 3)\n"))
	vars.nextSlotsRowSymbols = ConvertRawToSlots(vars.nextSlotsRow,vars.numberOfBoughtRows)
	#A REMPLACER
	print(vars.nextSlotsRowSymbols)
	#endregion

	#region INTERFACE GRAPHIQUE MATHIAS
	vars.nextSlotsRowSymbols
	open()
	#endregion

	#region CALCUL DU SCORE
	#Check for rows
	slotBoard = vars.nextSlotsRow
	for row in slotBoard[:vars.numberOfBoughtRows]:
		if row[0] == row[1] == row[2]:
			print(f"You won {vars.gambleAmount}x{vars.symbolMultiplier[row[0]]} = ${vars.gambleAmount*vars.symbolMultiplier[row[0]]}")
			vars.money += vars.gambleAmount*vars.symbolMultiplier[row[0]]
		else:
			print("Lost...")
	#endregion
	sleep(3)
	NewGame()

if __name__ == "__main__":
	NewGame()

