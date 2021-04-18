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
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

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
aces = ['Ace of Spades', 'Ace of Hearts', 'Ace of Clubs', 'Ace of Diamonds']
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
            print("Please enter the amount of money you will bring to the table:")
            starting_balance_input = int(input("$"))
            if starting_balance_input >= 50:
                starting_balance = starting_balance_input
                final_balance = starting_balance_input
                break
            else:
                print("\nA minimum of $50 is required, please try again\n")
        except:
            print("\nOnly whole numbers are allowed, please try again\n")  


def table_choice():
    global table_of_blackjack, bet_amount_per_round
    table_1 = random.randint(1, 88)
    table_2 = random.randint(1, 88)
    table_3 = random.randint(1, 88)
    
    print("\nThree tables are currently available for you to chose from:")
    print("Choice 1 - Table Number: {:02d},  $5 minimum bets".format(table_1))
    print("Choice 2 - Table Number: {:02d}, $10 minimum bets".format(table_2))
    print("Choice 3 - Table Number: {:02d}, $50 minimum bets".format(table_3))
    while True:
        try:
            table_chosen = int(input(
            "\nWhich choice of 1-3 would you like to make: "))
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
    dealer_names = ["Johnny", "Alexander", "Jordan", "Barnaby", "Max", "Nikolas",
    "Marty", "Page", "Dayton", "Godfrey"]

    random_choice = random.randint(0, len(dealer_names) - 1)
    dealer = dealer_names[random_choice]

    print(f"\nHi my name is {dealer} and I will be your dealer on " 
    f"Table #{table_of_blackjack} for this session.")
    print("Have a seat please remember the betting amount "
    +f"on Table #{table_of_blackjack} is ${bet_amount_per_round} per round.")


def win_message():
    global final_balance, round_finised
    print(f"\nThe dealers hidden card was {dealers_hidden_card()}")
    print("🎉 Congratulations you won ${} this round".format(bet_value * 2))
    final_balance += (bet_value * 2)
    round_finised = True

def loss_message():
    global final_balance, round_finised
    print(f"\nThe dealers hidden card was {dealers_hidden_card()}")
    print(f"😭 You lost ${bet_value} this round")
    round_finised = True

def draw_message():
    global final_balance, round_finised
    print(f"\nThe dealers hidden card was {dealers_hidden_card()}")
    print(f"🎭 It's a draw, your bets of ${bet_value} have been returned")
    final_balance += bet_value
    round_finised = True



def starting_bet():
    global bet_value, final_balance
    while True:
        try:
            print(f"\nYou currently have a balance of ${final_balance}")
            starting_bet = int(input("🎰 Please enter your starting bet from"
            +f" ${bet_amount_per_round} - $"))
            if starting_bet >= bet_amount_per_round:
                if starting_bet < final_balance:
                    bet_value += starting_bet
                    final_balance -= starting_bet
                    break
                elif starting_bet > final_balance:
                    print(f"Your bet of ${starting_bet} is larger than your " 
                    +f"balance of ${final_balance}, please try again")
            else:
                print(
                f"Your bet of ${starting_bet} was too small, please try again.")
        except:
            print("Please enter whole numbers thank you.\n")


def shuffled_deck_dealt_2_cards():
    global card_list, p_card_value, d_card_value, round_deck, cards_dealt
    round_deck = random.sample(deck, len(deck))
    cards_dealt = 2
    card_1_p = round_deck.pop(random.randint(0, len(round_deck) - 1))
    card_1_d = round_deck.pop(random.randint(0, len(round_deck) - 1))
    card_2_p = round_deck.pop(random.randint(0, len(round_deck) - 1))
    card_2_d = round_deck.pop(random.randint(0, len(round_deck) - 1))

    print(f"\nCard #1 for the player is: {card_1_p}")
    print(f"Card #2 for the player is: {card_2_p}\n")
    print(f"Card #1 for the dealer is: HIDDEN")
    print(f"Card #2 for the dealer is: {card_2_d}\n")

    card_list = [[card_1_p, card_2_p], [card_1_d, card_2_d]]

    p_card_value = sum([deck_values[card_1_p], deck_values[card_2_p]])
    d_card_value = sum([deck_values[card_1_d], deck_values[card_2_d]])


def dealers_hidden_card():
    return card_list[1][0]

def extra_bet():
    global bet_value, final_balance
    extra_bet_made = False
    while extra_bet_made == False:
        bet_choice = input(
        "\nWould you like to make another bet: 'y' for Yes, 'n' for No: ")
        if bet_choice.lower() == 'y':
            while True:
                try:
                    extra_bet = int(input("🎰 Please make a bet over or equal to"
                    +f" ${bet_amount_per_round} - $"))
                    if extra_bet >= bet_amount_per_round:
                        if extra_bet < final_balance:
                            final_balance -= extra_bet
                            bet_value += extra_bet
                            extra_bet_made = True
                            break
                        elif extra_bet > final_balance:
                            print(f"Your bet of ${extra_bet} is larger than your" 
                            +f" balance of ${final_balance}, please try again")
                    else:
                        print(
                        f"The bet amount must be over ${bet_amount_per_round}")
                except:
                    print("Only whole numbers are accepted, please try again")
        elif bet_choice.lower() == 'n':
            break
        else:
            print("The correct inputs are 'y' or 'n', please try again")


def extra_card_evaluation():
    global round_deck, final_balance, cards_dealt
    global p_card_value, d_card_value, round_finised
    if p_card_value < 21:
        while True:
            extra_card_choice = input(
            "\nWould you like an extra card: 'y' or 'n': ")
            print()
            if extra_card_choice.lower() == 'y':
                ace_checker_dealer()
                cards_dealt += 1
                extra_card_p = round_deck.pop(random.randint(0, len(round_deck) - 1))
                p_card_value += deck_values[extra_card_p]
                card_list[0].append(extra_card_p)
                print(f"\nCard #{cards_dealt} for the player" 
                +" is: {}".format(card_list[0][cards_dealt - 1]))
                if d_card_value < 17:
                    extra_card_d = round_deck.pop(random.randint(0, len(round_deck) - 1))
                    d_card_value += deck_values[extra_card_d]
                    card_list[1].append(extra_card_d)
                    print(f"Card #{cards_dealt} for the dealer"
                    +" is: {}\n".format(card_list[1][cards_dealt - 1]))
                elif d_card_value >= 17:
                    print("The dealer has chosen not to take an extra card\n")
                extra_bet()
                break                
            elif extra_card_choice.lower() == 'n':
                if d_card_value < 17:
                    cards_dealt += 1
                    extra_card_d = round_deck.pop(random.randint(0, len(round_deck) - 1))
                    d_card_value += deck_values[extra_card_d]
                    card_list[1].append(extra_card_d)
                    print(f"Card #{cards_dealt} for the dealer"
                    +" is: {}\n".format(card_list[1][cards_dealt - 1]))
                ace_checker_player()
                ace_checker_dealer()
                checker_of_21()
                evaluation_extra_card()
                break

def ace_checker_player():
    global p_card_value, aces

    p_ace_count = 0 
    for i in range(len(card_list[0])):
        for card in aces:
            if card in card_list[0]:
                aces.remove(card)
                p_ace_count += 1

    for i in range(p_ace_count):
        while True:
            ace_choice_p = input(
            "Would you like the Ace to be treated as a 1 or 11: ")
            if ace_choice_p == '1':
                p_card_value += 1
                break
            elif ace_choice_p == '11':
                p_card_value += 11
                break
            else:
                print("Whole number inputs only, please try again")


def ace_checker_dealer():
    global d_card_value, aces

    d_ace_count = 0
    for i in range(len(card_list[1])):
        for card in aces:
            if card in card_list[1]:
                aces.remove(card)
                d_ace_count += 1

    for i in range(d_ace_count):
        if d_card_value + 11 <= 21:
            d_card_value += 11
        else:
            d_card_value += 1
    

def checker_of_21():
    if p_card_value == d_card_value:
        draw_message()
    elif p_card_value == 21:
        if d_card_value == 21:
            draw_message()
        else:
            win_message()
    elif d_card_value == 21:
        if p_card_value == 21:
            draw_message()
        else:
            loss_message()
    elif p_card_value > 21:
        if p_card_value > d_card_value:
            loss_message()
        elif p_card_value < d_card_value:
            win_message()
    elif d_card_value > 21:
        if d_card_value > p_card_value:
            win_message()
        if d_card_value < p_card_value:
            loss_message()


def evaluation_extra_card():
    if round_finised != True:
        if p_card_value < d_card_value:
            loss_message()
        elif p_card_value > d_card_value:
            win_message()
        elif p_card_value == d_card_value:
            draw_message()

def table_refresh():
    global bet_value, round_deck, card_list, p_card_value
    global d_card_value, cards_dealt, round_finised, aces
    round_finised = False
    bet_value = 0
    round_deck = []
    card_list = []
    p_card_value = 0
    d_card_value = 0
    cards_dealt = 0
    aces = ['Ace of Spades', 'Ace of Hearts', 'Ace of Clubs', 'Ace of Diamonds']


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
        extra_bet()
        while round_finised == False:
            extra_card_evaluation()
        table_refresh()
        player_leave_table() 
    program_ending_draw()
    program_ending_win()
    program_ending_loss()


program_instructions()