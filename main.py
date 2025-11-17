#FICHIER MAIN OU LE JEU SE DEROULE :)
from fonctions import *
#region SYNC TO MAIN
#endregion

#region GAMBLE
betCoins = ("None",0)
while betCoins[0]!="Success":
	gambleAmount = input(f"Entrez la quantité d'$ que vous souhaitez parier\nYou currently have ${vars.money}\n")
	betCoins = BetCoins(gambleAmount, 1000)

	match betCoins[0]:
		case "FormatError":
			print("The format of the bet is incorrect !")
		case "NotEnough":
			print("You do not have enough money !")
		case "TooMuch":
			print("Your bet amount exceeds the upper limit !")
vars.money -= betCoins[1]
print(f"You gambled {gambleAmount}, and now have {vars.money}")
#endregion

#region Slot Logic
#vars.seed = CreateRandomSeed()
vars.nextSlotsRow = GenerateNextXSlots(3,3)
#A REMPLACER
vars.numberOfBoughtRows = int(input("Cmb de lignes ?(max 3)"))
vars.nextSlotsRowSymbols = ConvertRawToSlots(vars.nextSlotsRow,vars.numberOfBoughtRows)
#endregion

#region INTERFACE GRAPHIQUE

#endregion

#region CALCUL DU SCORE
#endregion