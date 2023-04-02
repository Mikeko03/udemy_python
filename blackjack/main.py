import random
from cards import list_of_cards, dict_of_cards


def draw():
    draw_card = random.choice(list_of_cards)
    return (draw_card, dict_of_cards[draw_card])


def deal_player():
    cont = True
    while cont:
        if len(player_hand) < 2:
            player = draw()
            player_hand.append(player[1])
            print(f"You got {player[0]}")
        else:
            print(f"Sum of your hand is {sum(player_hand)}")
            ans = input("Would you like another card? (Yes/No) ").lower()
            while ans not in ("yes", "y", "no", "n"):
                ans = input("Invalid input. Would you like another card? (Yes/No) ").lower()
            if ans in ("yes", "y"):
                player = draw()
                player_hand.append(player[1])
                print(f"You got {player[0]}")
            else:
                print(f"You stopped. Sum of your hand is {sum(player_hand)}")
                cont = False
        if sum(player_hand) == 21:
            print("Blackjack! Congratulations!")
            cont = False
        elif sum(player_hand) > 21:
            print(f"Sum of your hand is {sum(player_hand)}. You bust!")
            cont = False
        else:
            pass
def deal_dealer():
    cont = True
    while cont or sum(dealer_hand)<21:
        if len(dealer_hand) < 2:
            dealer = draw()
            dealer_hand.append(dealer[1])
            print(f"You got {dealer[0]}")
        else:
            print(f"Sum of dealer hand is {sum(dealer_hand)}")
        
            


if __name__ == "__main__":
    player_hand = []
    dealer_hand = []

    #deal_player()
    deal_dealer()
