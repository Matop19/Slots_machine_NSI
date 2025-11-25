with open('Casino.txt', 'r') as file:
    for line in file:
        print(line, end = "\n")

print("Welcome the the Casino!")
print("1 = Black Jack\n2 = Slot Machine\n3 = Pingo ")
n = input("Press 1,2,3 to start playing, or 'leave' to exit: ")
if n != 1:
    print("goodbye!")
    quit()
if n != 2:
    print("")
#if n ==1:
    #Code Black Jack Entry to be added
#if n ==2:
    #code Slot Machine entry to be added
#if n==3:
    #Code Pingo to be added
else:
    input("This is not a right value to have entered. Try again")
    





