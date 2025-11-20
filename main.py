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
		gambleAmount = input(f'''Entrez la quantité d'$ que vous souhaitez parier\nYou currently have ${vars.money}\nQuittez en entrant "LEAVE"\n''')
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
		#print("Seed",vars.seed)
	vars.nextSlotsRow = GenerateNextXSlots(3,3)
		#A REMPLACER
		#vars.numberOfBoughtRows = int(input("Cmb de lignes ?(max 3)\n"))
	vars.numberOfBoughtRows = 3
	vars.nextSlotsRowSymbols = ConvertRawToSlots(vars.nextSlotsRow,vars.numberOfBoughtRows)

	#endregion

	#region INTERFACE GRAPHIQUE MATHIAS
	print(vars.nextSlotsRow)
	#Pas de symboles pcq utilisé comme index
	ShowSymbols(vars.nextSlotsRow)


	#endregion

	#region CALCUL DU SCORE

	# vars.nextSlotsRow is now a list of tuples (columns)
	columns = vars.nextSlotsRow        # Example: [(3,5,7), (3,5,7), (3,5,7)]
	num_cols = len(columns)
	num_rows = len(columns[0])         # all columns have same height

	# We only check the number of rows the user has bought
	rows_to_check = vars.numberOfBoughtRows

	for r in range(rows_to_check):
		# Build the row from all columns
		row = [columns[c][r] for c in range(num_cols)]

		if row[0] == row[1] == row[2]:
			symbol = row[0]
			winnings = vars.gambleAmount * vars.symbolMultiplier[symbol]
			print(r''' .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |     _____    | || |      __      | || |     ______   | || |  ___  ____   | || |   ______     | || |     ____     | || |  _________   | |
| |    |_   _|   | || |     /  \     | || |   .' ___  |  | || | |_  ||_  _|  | || |  |_   __ \   | || |   .'    `.   | || | |  _   _  |  | |
| |      | |     | || |    / /\ \    | || |  / .'   \_|  | || |   | |_/ /    | || |    | |__) |  | || |  /  .--.  \  | || | |_/ | | \_|  | |
| |   _  | |     | || |   / ____ \   | || |  | |         | || |   |  __'.    | || |    |  ___/   | || |  | |    | |  | || |     | |      | |
| |  | |_' |     | || | _/ /    \ \_ | || |  \ `.___.'\  | || |  _| |  \ \_  | || |   _| |_      | || |  \  `--'  /  | || |    _| |_     | |
| |  `.___.'     | || ||____|  |____|| || |   `._____.'  | || | |____||____| | || |  |_____|     | || |   `.____.'   | || |   |_____|    | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' ''')
			print(f"You won {vars.gambleAmount}x{vars.symbolMultiplier[symbol]} = ${winnings}")
			vars.money += winnings


	#endregion

	# Wait for user to press a key
	input("")

	# Reset the game
	NewGame()


if __name__ == "__main__":
	NewGame()

