import random
from cards import list_of_cards, dict_of_cards


#draw a cards from the deck (not real deck)
def draw():
    draw_card = random.choice(list_of_cards)
    return (draw_card, dict_of_cards[draw_card])


# deals card to player and show what card it is
def deal_player():
    player = draw()
    player_cards.append(player[0])
    player_sum.append(player[1])
    return player_cards,player_sum


# deals card to dealer and show what card it is
def deal_dealer():
    dealer = draw()
    dealer_cards.append(dealer[0])
    dealer_sum.append(dealer[1])
    return dealer_cards,dealer_sum


# main function
def play_blackjack():
    ## first turn deals 2 cards
    for _ in range(2):
        deal_player()
        deal_dealer()

    print(f"Value of players hand is {sum(player_sum)}")
    print(f"CHEAT: value of dealers hand is {sum(dealer_sum)}\n")
    
    
    # dealing cards to player
    while True:
        # asks for what to do next
        ans = input("what to do next: (hit, stand)\n").lower()
        # hit == deals more cards
        if ans =="hit":
            deal_player()
            print(f"Value of players hand is {sum(player_sum)}\n")
            if sum(player_sum)>21:
                print("Bust dealer wins\n")
                return
        # stand enough cards
        elif ans == "stand":
            break
        else:
            print("choise MOFO\n")
    
    while sum(dealer_sum)<17:
        deal_dealer()
        print(f"CHEAT: value of dealer hand is {sum(dealer_sum)}\n")

        if sum(dealer_sum)>21:
            print("Bust player wins\n")
            return

    pl = sum(player_sum)
    dl = sum(dealer_sum)

    if pl < dl:
        print("dealer wins\n")
    elif pl > dl:
        print("player wins\n")
    else:
        print("tie\n")


if __name__ == "__main__":
    # initialize empty hands for lists of all the cards that dealer and player have
    player_cards = []
    dealer_cards = []
    player_sum = []
    dealer_sum = []
    play_blackjack()
