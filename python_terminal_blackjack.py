import random

def opening_banner():
    print("""
    
 /$$$$$$$  /$$                     /$$                               /$$      
| $$__  $$| $$                    | $$                              | $$      
| $$  \ $$| $$  /$$$$$$   /$$$$$$$| $$   /$$ /$$  /$$$$$$   /$$$$$$$| $$   /$$
| $$$$$$$ | $$ |____  $$ /$$_____/| $$  /$$/|__/ |____  $$ /$$_____/| $$  /$$/
| $$__  $$| $$  /$$$$$$$| $$      | $$$$$$/  /$$  /$$$$$$$| $$      | $$$$$$/ 
| $$  \ $$| $$ /$$__  $$| $$      | $$_  $$ | $$ /$$__  $$| $$      | $$_  $$ 
| $$$$$$$/| $$|  $$$$$$$|  $$$$$$$| $$ \  $$| $$|  $$$$$$$|  $$$$$$$| $$ \  $$
|_______/ |__/ \_______/ \_______/|__/  \__/| $$ \_______/ \_______/|__/  \__/
                                       /$$  | $$                              
                                      |  $$$$$$/                              
                                       \______/                               

               ♥️♠️♣️♦️ Welcome to Adam's Terminal BlackJack Game ♥️♠️♣️♦️
       This will be a 1v1 game where the player will play aginst the dealer
           🃏🃏🃏🃏 Have you got the skills to beat the dealer? 🃏🃏🃏🃏
                  """)  

#Decks
SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades'] 
RANKS = [
'2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

deck = []
for rank in RANKS: #creates a deck of cards
    for suit in SUITS:
        card = rank + ' of ' + suit
        deck.append(card)

deck_values = {} #dictionary of cards and their values, aces to be handled later
for rank in RANKS: #creates a dictionary of the deck and their values
    for suit in SUITS:
        card = rank + ' of ' + suit
        if rank in ('Jack', 'Queen', 'King'):
            value = 10
        elif rank == 'Ace':
            value = 0
        else:
            value = int(rank)
        deck_values.update({card: value})

#Global Variables
starting_balance = 0
final_balance = 0
bet_amount_per_round = 0

#Variables for the round
player_on_table = True
round_finised = False
bet_value = 0
round_deck = []
card_list = []
p_card_value = 0
d_card_value = 0
cards_dealt = 0


def starting_balance(): #starting balance brought to the table
    global starting_balance, final_balance
    while True:
        try:
            starting_balance_input = int(input(
            "Please enter the amount of money you will bring to the table: $"))
            starting_balance = starting_balance_input
            final_balance = starting_balance_input
            break
        except:
            print("\nOnly whole numbers are allowed, please try again\n")


def table_choice():
    global table_of_blackjack, bet_amount_per_round
    table_1 = random.randint(1, 88)
    table_2 = random.randint(1, 88)
    table_3 = random.randint(1, 88)
    print("\nThree tables are currently available for you to chose from:")
    print("Choice 1 - Table Number: {:02d},  $5 bets".format(table_1))
    print("Choice 2 - Table Number: {:02d}, $10 bets".format(table_2))
    print("Choice 3 - Table Number: {:02d}, $50 bets".format(table_3))
    while True:
        try:
            table_chosen = int(input(
            "\nWhich choice of 1-3 would you like to make: "))
            if table_chosen >= 1 and table_chosen <= 3:
                if table_chosen == 1:
                    bet_amount_per_round = 5
                    table_of_blackjack = table_1
                    break
                elif table_chosen == 2:
                    bet_amount_per_round = 10
                    table_of_blackjack = table_2
                    break
                elif table_chosen == 3:
                    bet_amount_per_round = 50
                    table_of_blackjack = table_3
                    break
            else:
               print("\nOnly whole numbers of 1-3 are allowed, please try again") 
        except:
            print("\nOnly whole numbers of 1-3 are allowed, please try again\n")


def dealer_introduction():
    dealer_names = ["Johnny", "Alexander", "Jordan", "Barnaby", "Max", "Nikolas"
    , "Marty", "Page", "Dayton", "Godfrey"]
    random_choice = random.randint(0, len(dealer_names) - 1)
    dealer = dealer_names[random_choice]
    print(f"\nHi my name is {dealer} and I will be your dealer on " 
    f"Table #{table_of_blackjack} for this session.")
    print("Have a seat please remember the betting amount "
    +f"on Table #{table_of_blackjack} is ${bet_amount_per_round} per round.")


def starting_bet():
    global bet_value, final_balance
    while True:
        try:
            print(f"\nYou currently have a balance of ${final_balance}")
            starting_bet = int(input("🎰 Please enter your starting bet from"
            +f" ${bet_amount_per_round} - $"))
            if starting_bet >= bet_amount_per_round:
                bet_value += starting_bet
                final_balance -= starting_bet
                break
            else:
                print(
                f"Your bet of ${starting_bet} was too small, please try again.")
        except:
            print("Please enter whole numbers thank you.\n")


def shuffled_deck_dealt_2_cards():
    global card_list, p_card_value, d_card_value, round_deck, cards_dealt
    round_deck = random.sample(deck, len(deck))
    card_1_p = round_deck.pop(random.randint(0, len(round_deck) - 1))
    card_2_p = round_deck.pop(random.randint(0, len(round_deck) - 1))
    card_1_d = round_deck.pop(random.randint(0, len(round_deck) - 1))
    card_2_d = round_deck.pop(random.randint(0, len(round_deck) - 1))
    cards_for_round = [[card_1_p, card_2_p], [card_1_d, card_2_d]]
    card_list += cards_for_round
    cards_dealt = 2
    p_card_value += sum([deck_values[card_1_p], deck_values[card_2_p]])
    d_card_value += sum([deck_values[card_1_d], deck_values[card_2_d]])


def printing_2_cards():
    print()
    print("Card #1 for the player is: {}".format(card_list[0][0]))
    print("Card #2 for the player is: {}".format(card_list[0][1]))
    print()
    print("Card #1 for the dealer is: {}".format(card_list[1][0]))
    print("Card #2 for the dealer is: hidden")
    print()


def dealers_hidden_card():
    return card_list[1][1]


def ace_checker():
    global p_card_value, d_card_value
    aces = ['Ace of Spades', 'Ace of Hearts', 'Ace of Clubs', 'Ace of Diamonds']
    
    p_ace_count = 0 
    for i in range(len(card_list[0])):
        for card in aces:
            if card in card_list[0]:
                p_ace_count += 1

    d_ace_count = 0
    for i in range(len(card_list[1])):
        for card in aces:
            if card in card_list[1]:
                d_ace_count += 1

    for i in range(p_ace_count):
        while True:
            ace_choice_p = input(
            "Would you like the Ace to be treated as a 1 or 11: "))
            if ace_choice_p == '1':
                p_card_value += 1
                break
            elif ace_choice_p == '11':
                p_card_value += 11
                break
            else:
                print("Whole number inputs only, please try again")

    for i in range(d_ace_count):
        if d_card_value + 11 <= 21:
            d_card_value += 11
        else:
            d_card_value += 1


def extra_bet():
    global bet_value, final_balance
    print("The time has come to make another bet")
    while True:
        bet_choice = input(
        "\nWould you like to make another bet: 'y' for Yes, 'n' for No: ")
        if bet_choice.lower() == 'y':
            while True:
                try:
                    extra_bet = int(input(
                    f"🎰 Please make a bet over ${bet_amount_per_round} - $"))
                    if extra_bet >= bet_amount_per_round:
                        final_balance -= extra_bet
                        bet_value += extra_bet
                        break
                    else:
                        print(
                        f"The bet amount must be over ${bet_amount_per_round}")
                except:
                    print("Only whole numbers are accepted, please try again")
        elif bet_choice.lower() == 'n':
            break
        else:
            print("The correct inputs are 'y' or 'n', please try again")


def checker_of_21():
    global final_balance, round_finised
    if d_card_value != 21:
        if p_card_value == 21:
            print(f"\nThe dealers hidden card was {dealers_hidden_card()}")
            print(
            "🎉 Congratulations you won ${} this round".format(bet_value * 2))
            final_balance += (bet_value * 2)
            round_finised = True
        elif p_card_value > 21:
            if d_card_value < 21:
                print(f"\nThe dealers hidden card was {dealers_hidden_card()}")
                print(f"😭 You lost ${bet_value} this round")
                round_finised = True
            elif d_card_value > 21:
                print(f"\nThe dealers hidden card was {dealers_hidden_card()}")
                print(
                f"🎭 It's a draw, your bets of ${bet_value} have been returned")
                final_balance += bet_value
                round_finised = True
    else:
        if p_card_value == 21:
            print(f"\nThe dealers hidden card was {dealers_hidden_card()}")
            print(f"🎭 It's a draw, your bets of ${bet_value} have been returned")
            final_balance += bet_value
            round_finised = True


def extra_card_evaluation():
    global round_deck, final_balance, cards_dealt
    global p_card_value, d_card_value, round_finised
    if p_card_value < 21:
        while True:
            extra_card_choice = input(
            "\nWould you like an extra card: 'y' or 'n': ")
            print()
            if extra_card_choice.lower() == 'y':
                cards_dealt += 1
                extra_card_p = round_deck.pop(random.randint(0, len(round_deck) - 1))
                p_card_value += deck_values[extra_card_p]
                card_list[0].append(extra_card_p)
                print(f"\nCard #{cards_dealt} for the player" 
                +" is: {}".format(card_list[0][2]))
                if d_card_value < 18:
                    extra_card_d = round_deck.pop(random.randint(0, len(round_deck) - 1))
                    d_card_value += deck_values[extra_card_d]
                    card_list[1].append(extra_card_d)
                    print(f"Card #{cards_dealt} for the dealer"
                    +" is: {}\n".format(card_list[1][2]))
                elif d_card_value >= 18:
                    print("The dealer has chosen not to take an extra card")
                break
            elif extra_card_choice.lower() == 'n':
                if p_card_value < d_card_value:
                    print(f"\nThe dealers hidden card was {dealers_hidden_card()}")
                    print(f"😭 You lost ${bet_value} this round")
                    round_finised = True
                    break
                elif p_card_value > d_card_value:
                    print(f"\nThe dealers hidden card was {dealers_hidden_card()}")
                    print(
                    f"🎉 Congratulations you won ${bet_value * 2} this round")
                    final_balance += (bet_value * 2)
                    round_finised = True
                    break


def table_refresh():
    global bet_value, round_deck, card_list, p_card_value
    global d_card_value, cards_dealt, round_finised
    round_finised = False
    bet_value = 0
    round_deck = []
    card_list = []
    p_card_value = 0
    d_card_value = 0
    cards_dealt = 0


def player_leave_table():
    global player_on_table
    while True:
        choice = input("\nWould you like to continue at the table"
        + " 'y' to continue or 'n' to leave: ")
        if choice.lower() == 'y':
            player_on_table = True
            break
        elif choice.lower() == 'n':
            player_on_table = False
            break
        else:
            print("The correct inputs are 'y' or 'n' please try again.")
        

def program_ending_draw():
    if final_balance == starting_balance:
        print(f"You have left with the same amount you started with.")
        print(f"Come again soon.\n")


def program_ending_win():
    if final_balance > starting_balance:
        print(f"You started with ${starting_balance} and you have left" 
        + f" with ${final_balance}.")
        print(f"🥳 That is a gain of ${final_balance - starting_balance}.")
        print("""

 /$$     /$$                       /$$      /$$ /$$          
|  $$   /$$/                      | $$  /$ | $$|__/          
 \  $$ /$$/$$$$$$  /$$   /$$      | $$ /$$$| $$ /$$ /$$$$$$$ 
  \  $$$$/$$__  $$| $$  | $$      | $$/$$ $$ $$| $$| $$__  $$
   \  $$/ $$  \ $$| $$  | $$      | $$$$_  $$$$| $$| $$  \ $$
    | $$| $$  | $$| $$  | $$      | $$$/ \  $$$| $$| $$  | $$
    | $$|  $$$$$$/|  $$$$$$/      | $$/   \  $$| $$| $$  | $$
    |__/ \______/  \______/       |__/     \__/|__/|__/  |__/
                                                                                                                         
""")

def program_ending_loss():
    if final_balance < starting_balance:
       print(f"You started with ${starting_balance} and you have left" 
        + f" with ${final_balance}.") 
       print(f"😔 That is a loss of ${final_balance - starting_balance}.") 
       print("""

 /$$     /$$                       /$$                                    
|  $$   /$$/                      | $$                                    
 \  $$ /$$/$$$$$$  /$$   /$$      | $$        /$$$$$$   /$$$$$$$  /$$$$$$ 
  \  $$$$/$$__  $$| $$  | $$      | $$       /$$__  $$ /$$_____/ /$$__  $$
   \  $$/ $$  \ $$| $$  | $$      | $$      | $$  \ $$|  $$$$$$ | $$$$$$$$
    | $$| $$  | $$| $$  | $$      | $$      | $$  | $$ \____  $$| $$_____/
    | $$|  $$$$$$/|  $$$$$$/      | $$$$$$$$|  $$$$$$/ /$$$$$$$/|  $$$$$$$
    |__/ \______/  \______/       |________/ \______/ |_______/  \_______/
                                                                          
 """)


def program_instructions():
    opening_banner()
    starting_balance()
    table_choice()
    dealer_introduction()
    while player_on_table == True:
        starting_bet()
        shuffled_deck_dealt_2_cards()
        printing_2_cards()
        ace_checker()
        extra_bet()
        checker_of_21()
        while round_finised == False:
            ace_checker()
            extra_card_evaluation()
            if round_finised == False:
                extra_bet()
                checker_of_21()
        table_refresh()
        player_leave_table()  
    program_ending_draw()
    program_ending_win()
    program_ending_loss()

#Runs the program
program_instructions()

