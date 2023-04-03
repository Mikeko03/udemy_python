from logo import str, str2
import random

print(str2,"\n")

## nastavanie naročnosti
def set_dif():
    dif = input("How hard game you want to play? (easy or hard)\n").lower()
    while dif  not in ("easy", "hard"):
        dif = input("Invalid input. What difficulty you want? (easy or hard) ").lower()
    if dif == "easy":
        return 10
    elif dif == "hard":
        return 5


def guesser():
    return int(input("What is your guess: "))


def number_generator():
    return random.randint(1,100)


def game():
    number_of_turns, guessed_number= set_dif(), number_generator()
    print(f"psst{guessed_number}")
    print(f"Turns left {number_of_turns}\n")
    while number_of_turns > 0:
        guess = guesser()
        if guess > guessed_number:
            print("Too HIGH")
            print(f"You have {number_of_turns} turns left\n")
        elif guess < guessed_number:
            print("Too LOW")
            print(f"You have {number_of_turns} turns left\n")
        else:
            print("You guessed RIGHT")
            return
        number_of_turns-=1
    print("You lost, all turns are gone")
        
if __name__ == "__main__":
    game()
