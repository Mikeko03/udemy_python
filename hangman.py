from hangman_words import word_list as wl
import random

choosen_word = random.choice(wl)
print(f"Your choosen word is {choosen_word}")

def guess():
    return input("Choose your letter: ").lower()

alive = True

lst = ["_" for _ in choosen_word]
lst2 = []
live = 6

while alive: 
    g = guess()
    
    if g in lst2:
        print(f"you already picked {g}, choose another letter\n")
    else:
        lst2.append(g)
        for idx, x in enumerate(choosen_word):
            if g == x:
                lst[idx]=x
        if g not in choosen_word:
            live = live - 1
            print(f">>>{g} is not in the choosen word<<<")
        print("\n", ' '.join(lst).upper(),"\n" )
        print(f"You have {live} lives\n___________________________")

        if live == 0:
            print("You lost")
            alive = False


        if "_" not in lst:
            print("\n\n ------------------\n |YOU WON, HURAAAA|\n ------------------")
            alive = False