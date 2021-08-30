import random
from cards import Card


def init_cards():
    global deck, p_hand, c_hand, up_card, active_suit, active_rank
    deck = []
    # 创建一副牌
    for suit_id in range(1, 5):
        for rank_id in range(1, 14):
            new_card = Card(suit_id, rank_id)
            # 让 8 的分值变为50
            if new_card.rank == 8:
                new_card.value = 50
            deck.append(Card(suit_id, rank_id))
    p_hand = []
    c_hand = []
    for i in range(5):
        p_card = random.choice(deck)
        deck.remove(p_card)
        p_hand.append(p_card)
        c_card = random.choice(deck)
        deck.remove(c_card)
        c_hand.append(c_card)
    up_card = random.choice(deck)
    deck.remove(up_card)
    active_suit = up_card.suit
    active_rank = up_card.rank


def player_turn():
    global deck, p_hand, blocked, up_card, active_suit
    valid_play = False
    is_eight = False
    print("\nYour hand: ", end='')
    for card in p_hand:
        print(card.short_name, end=' ')
    print("   Up card:", up_card.short_name, end='')
    if up_card.rank == '8':
        print("    Suit:", active_suit, end='')
    print("\nWhat would you like to do? ", end='')
    response = input("Type a card to play or 'Draw' to take a card: ")
    while not valid_play:   # 在玩家键入有效的内容之前一直循环
        selected_card = None
        while selected_card == None:
            # 抽牌
            if response.lower() == 'draw':
                valid_play = True
                if len(deck) > 0:
                    card = random.choice(deck)
                    p_hand.append(card)
                    deck.remove(card)
                    print("You drew", card.short_name)
                else:
                    print("There are no cards left in the deck")
                    blocked += 1
                return  # 当抽玩牌后，返回到主循环
            else:
                for card in p_hand:
                    if response.upper() == card.short_name:
                        selected_card = card
                if selected_card == None:
                    response = input("You don't have that card. Try again: ")

        if selected_card.rank == '8':
            valid_play = True
            is_eight = True
        elif selected_card.suit == active_suit:
            valid_play = True
        elif selected_card.rank == up_card.rank:
            valid_play = True

        if not valid_play:
            response = input("That's not a legal play. Try again: ")

    p_hand.remove(selected_card)
    up_card = selected_card
    active_suit = up_card.suit
    print(
        f"You played the {selected_card.short_name} ({selected_card.long_name})")
    if is_eight == True:
        print("\nYour hand: ", end='')
        for card in p_hand:
            print(card.short_name, end=' ')
        get_new_suit()


def get_new_suit():
    global active_suit
    got_suit = False
    suit = input("   Pick a suit: ")
    while not got_suit:
        if suit.lower() == 'd':
            active_suit = "Diamods"
            got_suit = True
        elif suit.lower() == 's':
            active_suit = "Spades"
            got_suit = True
        elif suit.lower() == 'h':
            active_suit = "Hearts"
            got_suit = True
        elif suit.lower() == 'c':
            active_suit = "Clubs"
            got_suit = True
        else:
            suit = input("Not a valid suit. Try again: ")
    print("You picked", active_suit)


def computer_turn():
    global c_hand, deck, up_card, active_suit, blocked
    options = []
    for card in c_hand:
        # 有8出8
        if card.rank == '8':
            c_hand.remove(card)
            up_card = card
            print(
                f"Computer played {card.short_name} ({card.long_name})", end='')
            # 花色牌数：【方块， 红桃， 黑桃， 梅花】
            suit_totals = [0, 0, 0, 0]
            # 统计每种花色的牌数
            for suit in range(1, 5):
                for card in c_hand:
                    if card.suit_id == suit:
                        suit_totals[suit - 1] += 1
            long_suit = 0
            for i in range(4):
                if suit_totals[i] > long_suit:
                    long_suit = i
            if long_suit == 0:
                active_suit = "Diamonds"
            if long_suit == 1:
                active_suit = "Hearts"
            if long_suit == 2:
                active_suit = "Spades"
            if long_suit == 3:
                active_suit = "Clubs"
            print(" and changes suit to", active_suit)
            print(f"Computer has {len(c_hand)} cards left")
            return
        else:
            # 检查可能出哪些牌
            if card.suit == active_suit:
                options.append(card)
            elif card.rank == up_card.rank:
                options.append(card)

    if len(options) > 0:
        best_play = options[0]
        # 判断哪个选择最佳（最高分值）
        for card in options:
            if card.value > best_play.value:
                best_play = card
        # 出牌
        c_hand.remove(best_play)
        up_card = best_play
        active_suit = up_card.suit
        print(
            f"Computer played {best_play.short_name} ({best_play.long_name})")
    else:
        if len(deck) > 0:
            next_card = random.choice(deck)
            c_hand.append(next_card)
            deck.remove(next_card)
            print("Computer draws a card")
        else:
            print("Computer is blocked")
            blocked += 1
    print(f"Computer has {len(c_hand)} cards left")


print("Crazy Eights", end='')

done = False
p_total = c_total = 0
while not done:
    game_done = False
    blocked = 0
    init_cards()
    while not game_done:
        player_turn()
        if len(p_hand) == 0:
            game_done = True
            print()
            print("You won!")
            # 显示游戏得分
            p_points = 0
            for card in c_hand:
                p_points += card.value
            p_total += p_points
            print(f"You got {p_points} points from computer's hand")
        if not game_done:
            computer_turn()
        if len(c_hand) == 0:
            game_done = True
            print()
            print("Computer won!")
            c_points = 0
            for card in p_hand:
                c_points += card.value
            c_total += c_points
            print(f"Computer got {c_points} points from your hand")
        if blocked >= 2:
            game_done = True
            print("Both players blocked. GAME OVER")
            p_points = 0
            for card in c_hand:
                p_points += card.value
            p_total += p_points
            c_points = 0
            for card in p_hand:
                c_points += card.value
            c_total += c_points
            print(f"You got {p_points} points from computer's hand")
            print(f"Computer got {c_points} points from your hand")
    play_again = input("Play again (Y/N)? ")
    if play_again.lower().startswith('y'):
        done = False
        print(f"\nSo far, you have {p_total} points")
        print(f"and the computer has %i points.\n")
    else:
        done = True

print("\nFinal Score:")
print(f"You: {p_total}     Computer: {c_total}")
