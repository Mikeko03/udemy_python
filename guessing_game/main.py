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
    number_of_turns = set_dif()
    guessed_number = number_generator()
    print(f"psst{guessed_number}")
    print(f"Turns left {number_of_turns}\n")
    guess = guesser()
    while guessed_number != guess:
        if guess > guessed_number:
            print("Too high")
            number_of_turns -=1
            print(f"Turns left {number_of_turns}\n")
            guess = guesser()
        elif guess < guessed_number:
            print("Too low")
            number_of_turns -=1
            print(f"Turns left {number_of_turns}\n")
            guess = guesser()
    print("You guessed Right!!")
        
if __name__ == "__main__":
    game()
