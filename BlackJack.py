from random import randint
# Basic variables
print("Welcome to The Game!")
current_dealer_points = 1000
current_user_points = 1000
round_counter = 0
is_game_continue = True
#Main game loop
while is_game_continue:
    # increase counter every loop 
    round_counter += 1
    print("############################")
    print("Round",round_counter)
    print("Current User Points:", current_user_points)
    print("Current Dealer Points:", current_dealer_points)
    print("############################")
    bet = int(input("Please place a maximum of "+str(current_user_points)+" bet: "))
    # bet control
    while bet > current_user_points:
        print("Please choose valid bet amounth")
        bet = int(input("Please place a maximum of "+str(current_user_points)+" bet: "))
    #Other basic variables
    dealer_total = 0
    dealer_cards = ""
    user_total = 0
    user_cards = ""
    ace_max = 11
    user_ace_11 = False
    dealer_ace_11 = False
    # dealer draw 2 cards and I store these string format and also store total value of cards
    for i in range(2):
        card = min(10,randint(1,13))
        if i == 0:
            # these lines for appropriate format. (card-card-card-...)
            dealer_cards = dealer_cards + str(card)
        else:
            dealer_cards = dealer_cards + "-" + str(card)
        if i == 1:
            # I hide first card so I need second card information
            dealer_second_card = str(card)
        # These lines for setting the ace value
        if card == 1 and dealer_total+ace_max <= 21:
            dealer_total += ace_max
            dealer_ace_11 = True
        else:
            dealer_total += card
        if dealer_total > 21 and dealer_ace_11 == True:
            dealer_total -= 10
            dealer_ace_11 = False
    print("Dealer has: ?-"+dealer_second_card)
    # user draw 2 card
    for j in range(2):
        card = min(10,randint(1,13))
        if j == 0:
            user_cards = user_cards + str(card)
        else:
            user_cards = user_cards + "-" + str(card)
        if card == 1 and user_total+ace_max <= 21:
            user_total += ace_max
            user_ace_11 = True
        else:
            user_total += card
        if user_total > 21 and user_ace_11 == True:
            user_total -= 10
            user_ace_11 = False
    # I write the cards and total
    print("User has: "+user_cards+" (total: "+str(user_total)+")")
    print("Do you want to draw just one more card and double the bet? (y,n)")
    double_bet = input()
   
    if double_bet == "y":
        #First challenge accepted
        bet *= 2
        # extra draw and ace control
        card = min(10,randint(1,13))
        user_cards = user_cards + "-" + str(card)
        if card == 1 and user_total+ace_max <= 21:
            user_total += ace_max
            user_ace_11 = True
        else:
            user_total += card
        if user_total > 21 and user_ace_11:
            user_total -= 10
            user_ace_11 = False
        print("User has: "+user_cards+" (total: "+str(user_total)+")")
        # if total value exceed the 21 you lose
        if user_total > 21:
            print("Dealer win this round")
            current_user_points -= bet
            current_dealer_points += bet
        else:
            # If you haven't exceeded it, now it's the dealer's turn.
            dealer_turn = True
            print("Dealer's turn")
            print("Dealer has: "+dealer_cards+" (total: "+str(dealer_total)+")")
            while dealer_turn:
                # The dealer's cycle continues until the dealer exceeds 21 or has more points than the player but less than 21.
                if dealer_total > user_total:
                    print("Dealers win this round")
                    dealer_turn = False
                    current_dealer_points += bet
                    current_user_points -= bet
                else:
                    card = min(10,randint(1,13))
                    print("New card: "+ str(card))
                    dealer_cards = dealer_cards + "-" + str(card)
                    if card == 1 and dealer_total+ace_max <= 21:
                        dealer_total += ace_max
                        dealer_ace_11 = True
                    else:
                        dealer_total += card
                    if dealer_total > 21 and dealer_ace_11:
                        dealer_total -= 10
                        dealer_ace_11 = False
                    print("Dealer has: "+dealer_cards+" (total: "+str(dealer_total)+")")
                    if dealer_total > 21:
                        print("User win this round!")
                        dealer_turn = False
                        current_user_points += bet
                        current_dealer_points -= bet
                    elif dealer_total > user_total:
                        print("Dealer win this round")
                        dealer_turn = False
                        current_user_points -= bet
                        current_dealer_points += bet
                    elif dealer_total == user_total:
                        dealer_turn = False
    else:
        user_turn = True
        user_lose = False
        while user_turn:
            print("Do you want another card? (y,n)")
            another_card = input()
            if another_card == "y":
                card = min(10,randint(1,13))
                print("New card: "+ str(card))
                user_cards = user_cards + "-" + str(card)
                if card == 1 and user_total+ace_max <= 21:
                    user_total += ace_max
                    user_ace_11 =True
                else:
                    user_total += card
                if user_total > 21 and user_ace_11 == True:
                    user_total -= 10
                    user_ace_11 = False
                print("User has: "+user_cards+" (total: "+str(user_total)+")")
                if user_total > 21:
                    print("Dealer win this round")
                    user_lose = True
                    user_turn = False
                    current_user_points -= bet
                    current_dealer_points += bet
            else:
                user_turn = False
        if user_lose == False:
            dealer_turn = True
            print("Dealer's turn")
            print("Dealer has: "+dealer_cards+" (total: "+str(dealer_total)+")")
            while dealer_turn:
            # The dealer's cycle continues until the dealer exceeds 21 or has more points than the player but less than 21.
                if dealer_total > user_total:
                    print("Dealer win this round")
                    dealer_turn = False
                    current_user_points -= bet
                    current_dealer_points += bet
                else:
                    card = min(10,randint(1,13))
                    print("New card: "+ str(card))
                    dealer_cards = dealer_cards + "-" + str(card)
                    if card == 1 and dealer_total+ace_max <= 21:
                        dealer_total += ace_max
                        dealer_ace_11 = True
                    else:
                        dealer_total += card
                    if dealer_total > 21 and dealer_ace_11 == True:
                        dealer_total -= 10
                        dealer_ace_11 = False
                    print("Dealer has: "+dealer_cards+" (total: "+str(dealer_total)+")")
                    if dealer_total > 21:
                        print("User win this round!")
                        dealer_turn = False
                        current_user_points += bet
                        current_dealer_points -= bet
                    elif dealer_total > user_total:
                        print("Dealer win this round")
                        dealer_turn = False
                        current_user_points -= bet
                        current_dealer_points += bet
                    elif dealer_total == user_total:
                        dealer_turn = False
    lets_go = input("Press Enter to continue...")
    if current_user_points <= 0:
        print("DEALER WIN THE GAME")
        is_game_continue = False
    elif current_dealer_points <= 0:
        print("USER WIN THE GAME")
        is_game_continue = False   
            
