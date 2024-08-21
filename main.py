# Dice sum probability calculator
# Författare: Hannes_Tinnis
# Datum: 2024-08-21

import os 
os.system("cls")

def main():
    user_input = [int(x) for x in input("Skriv in 2 siffror på mängden sidor av 2 olika tärningar ").split(" ")]    #Input, ger användaren möjlighet att skriva in 2 olika tal sedan splitta dem.
    min_dice = min(user_input)  # hittar det mindre av de två siffrorna i listan user_input
    max_dice = max(user_input)  # hittar det större av de två siffrorna i listan user_input

    for sum in range(min_dice + 1, max_dice + 2): #for loop, Den största summan som kan kastas är max_dice + min_dice, så max_dice + 1 ser till att alla möjliga summor beaktas. 
        print(sum)
  

if __name__ == "__main__":
    main()