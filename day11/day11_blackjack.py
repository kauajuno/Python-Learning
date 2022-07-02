import random


def check_blackjack(player, opponent):
    """
    Checks all the conditions needed for a blackjack game to end
    :param player:
    :param opponent:
    :return:
    """
    sum_player = sum(player)
    sum_opponent = sum(opponent)
    if sum_player == 21 and sum_opponent == 21:
        print("Double blackjack! It's a draw!")
        return True
    elif sum_player == 21:
        print("Player's blackjack! You win!")
        return True
    elif sum_opponent == 21:
        print("Opponent's blackjack! You lose!")
        return True
    elif sum_player > 21:
        print("Overflow! You lose!")
        return True
    elif sum_opponent > 21:
        print("Opponent's overflow! You win!")
        return True
    return False


def draw_card():
    """
    Chooses a random card from the deck and returns it
    :return:
    """
    return random.choice(deck)


should_stop = False
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_hand = [draw_card() for i in range(2)]
pc_hand = [draw_card() for j in range(2)]

print(f"Your hand: {player_hand}, PC hand: {pc_hand}")

while not should_stop:
    should_stop = check_blackjack(player_hand, pc_hand)
    if should_stop is False:
        draw_choice = input("Want to draw another card? y/n\n")
        if draw_choice == 'n':
            while sum(pc_hand) < 17:
                pc_hand.append(draw_card())
            should_stop = check_blackjack(player_hand, pc_hand)
        else:
            player_hand.append(draw_card())
            if sum(pc_hand) < 17:
                pc_hand.append(draw_card())
        print(f"Your hand: {player_hand}, PC hand: {pc_hand}")
