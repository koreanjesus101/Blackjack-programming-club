# ^ Initialize the deck of cards reference
deck_of_cards = [
    # Hearts
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,  # Jack, Queen, King = 10, Ace = 11
    # Diamonds
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
    # Clubs
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
    # Spades
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11
]

import random
import time

player_balance = 100
def place_bet():
    global player_balance
    while True:
        try:
            bet = int(input(f"Your current balance is ${player_balance}. Enter your bet amount: $"))
            if bet > 0 and bet <= player_balance:
                return bet
            else: 
                print(f"Invalid bet. PLease bet an amount between $1 and ${player_balance}.")
        except ValueError:
            print("Invalid input. PLease enter a valid number.")

while True:
    # ^ Shuffle the deck at the start of each game
    if player_balance = 0
        print("You have no more money. Game Over!")
        break
    shuffled_deck = deck_of_cards.copy()
    random.shuffle(shuffled_deck)

    # ^ Initialize hands for dealer and player
    dealer_hand = []
    player_hand = []
    player_hand.append(shuffled_deck.pop())
    dealer_hand.append(shuffled_deck.pop())
    player_hand.append(shuffled_deck.pop())
    dealer_hand.append(shuffled_deck.pop())
    
    # * Welcome message
    print("\n--- Welcome to Blackjack ---")

    bet = place_bet()

    def calculate_hand_value(hand):
        # & Calculate the total value of a hand
        value = sum(hand)
        # & Adjust for Aces if value is over 21
        aces = hand.count(11)
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value

    def display_hands(player_hand, dealer_hand, reveal_dealer=False):
        # * Display the current hands of player and dealer
        print("\n--- Current Hands ---")
        print(f"Player's hand: {player_hand} (Value: {calculate_hand_value(player_hand)})")
        if reveal_dealer:
            print(f"Dealer's hand: {dealer_hand} (Value: {calculate_hand_value(dealer_hand)})")
        else:
            print(f"Dealer's hand: [{dealer_hand[0]}, '?']")
        print("----------------------\n")

    def suspenseful_display(message):
        # * Display messages with a suspenseful effect
        for char in message:
            print(char, end='', flush=True)
            time.sleep(0.04)
        print()

    # * Display initial hands
    display_hands(player_hand, dealer_hand)

    # & Player's turn
    while calculate_hand_value(player_hand) < 21:
        # * Ask player for action
        action = input("Do you want to 'hit' or 'stand'? ").lower()
        while action not in ['hit', 'stand']:
            print("Invalid input. Please enter 'hit' or 'stand'.")
            action = input("Do you want to 'hit' or 'stand'? ").lower()
        if action == 'hit':
            # ^ Player hits and draws a new card
            new_card = shuffled_deck.pop()
            player_hand.append(new_card)
            suspenseful_display(f"Player hits and draws a {new_card}...")
            display_hands(player_hand, dealer_hand)
        elif action == 'stand':
            # * Player stands
            suspenseful_display("Player stands...")
            break

    # & Dealer's turn
    while calculate_hand_value(dealer_hand) < 17:
        # ^ Dealer hits and draws a new card
        new_card = shuffled_deck.pop()
        dealer_hand.append(new_card)
        suspenseful_display(f"Dealer hits and draws a {new_card}...")

    # * Display final hands
    display_hands(player_hand, dealer_hand, reveal_dealer=True)

    # ^ Determine the outcome
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    # * Display final result
    print("\n--- Final Result ---")
    if player_value > 21 and dealer_value > 21:
        suspenseful_display("Both player and dealer bust! It's a tie.")
    elif player_value > 21:
        suspenseful_display("Player busts! Dealer wins.")
    elif dealer_value > 21:
        suspenseful_display("Dealer busts! Player wins.")
    elif player_value > dealer_value:
        suspenseful_display("Player wins!")
    elif player_value < dealer_value:
        suspenseful_display("Dealer wins!")
    else:
        suspenseful_display("It's a tie!")
    print("----------------------")
    
    # * Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no) ").lower()
    while play_again not in ['yes', 'no']:
        print("Invalid input. Please enter 'yes' or 'no'.")
        play_again = input("Do you want to play again? (yes/no) ").lower()
    if play_again != 'yes':
        # * Goodbye message
        print(f" Thanks for playing! Goodbye! You leave with ${player_balance}.")
        break
