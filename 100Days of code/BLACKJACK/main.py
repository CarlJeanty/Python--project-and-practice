import random 

card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



"""Computer decision Function"""
def cp_choice(computer_hand):
    hit_or_stand_cp = True
    while hit_or_stand_cp:
        if 21-sum(computer_hand) >random.randint(2,8):
            computer_hand.append(int(random.choice(card)))
            if sum(computer_hand)> 21 and 11 in computer_hand:
                computer_hand.append(int(-10))
        else:
            hit_or_stand_cp = False    


"""Player decision function to add another card"""
def player(player_hand):
    hit_or_stand = True
    while hit_or_stand:
        player_choice = input("Would you like to receive another card 'y' or 'n'").lower()
        if player_choice == "y":
            player_hand.append(int(random.choice(card)))
            if sum(player_hand)> 21 and 11 in player_hand:
                player_hand.append(int(-10))
            if sum(player_hand)>=21:
                hit_or_stand = False 
                print(player_hand)
        else:
            hit_or_stand = False 
        print(player_hand)
def decision(player_hand,computer_hand):  
    if sum(player_hand) > sum(computer_hand) and sum(player_hand) <=21:
        print((f"Player wins {player_hand} = {sum(player_hand)} beats {computer_hand} = {sum(computer_hand)}"))
    elif sum(player_hand) < sum(computer_hand) and sum(computer_hand) <=21:
        print((f"Player {player_hand} = {sum(player_hand)} loses to {computer_hand} = {sum(computer_hand)}"))
    elif sum(player_hand) > 21 and sum(computer_hand) <=21:
        print(f"Bust player {player_hand} = {sum(player_hand)}, dealer wins {computer_hand} = {sum(computer_hand)}")
    elif sum(computer_hand) > 21 and sum(player_hand) <=21:
        print(f"Bust dealer {computer_hand}={sum(computer_hand)} ,{player_hand}={sum(player_hand)} player wins")
    elif sum(player_hand) == sum(computer_hand):
        print(f"Push, Tie, cp{computer_hand}{sum(computer_hand)} equal too p{player_hand}{sum(player_hand)}")
    else:
        print(" 2 losers")
def start_game():
    computer_hand = [int(random.choice(card)), int(random.choice(card))]
    player_hand = [int(random.choice(card)), int(random.choice(card))]
    print(f"Your hand is: {player_hand}\n computer hand is {random.choice(computer_hand)}")
    player(player_hand=player_hand)
    if sum(player_hand) <21:
        cp_choice(computer_hand=computer_hand)
    print(f"your final hand is {player_hand}")
    print(f"computer final hand is {computer_hand}")
    decision(player_hand=player_hand,computer_hand=computer_hand)
    play_again = input("Would you like to play a game of blackjack 'y' or 'n' ?" ).lower()
    if play_again =='y':
        start_game()
    else:
        print("Thank you for playing, the house always wins")

start_game()