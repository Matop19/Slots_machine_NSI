#FICHIER MAIN OU LE JEU SE DEROULE :)
from fonctions import *

#region GAMBLE
""" betCoins = ("None",0)
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
print(f"You gambled {gambleAmount}, and now have {vars.money}") """
#endregion

slots = GenerateNextXSlots(3,3)
print(ConvertRawToSlots(slots,1))