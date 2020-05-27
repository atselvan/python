"""
Blackjack
"""
import random
import os

SPADE_SUIT = "\u2660"
HEART_SUIT = "\u2665"
DIAMOND_SUIT = "\u2666"
CLUB_SUIT = "\u2663"

SUITS = [SPADE_SUIT, HEART_SUIT, DIAMOND_SUIT, CLUB_SUIT]


class EmptyDeckError(AttributeError):

    def __init__(self, arg):
        AttributeError.__init__()
        self.arg = arg


class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print(f"{self.value}{self.suit}")

    def __str__(self):
        return f"{self.value}{self.suit}"


class Deck:

    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in SUITS:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))

    def show(self):
        os.system("clear")
        for card in self.cards:
            card.show()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if len(self.cards) > 0:
            return self.cards.pop(0)
        raise EmptyDeckError('No more cards in the deck to draw')


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card: Card):
        self.cards.append(card)
        if card.value == 1:
            self.value += 11
        elif card.value <= 10:
            self.value += card.value
        else:
            self.value += 10

        # Check for Aces
        if card.value == 1:
            self.aces += 1

    def adjust_for_aces(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self, initial_value):
        self.value = initial_value  # Initial value for chips
        self.bet = 0

    def win_bet(self):
        self.value += self.bet

    def lose_bet(self):
        self.value -= self.bet

    def __str__(self):
        return str(self.value)


class Player:

    def __init__(self, name: str):
        self.name = name
        self.hand = Hand()
        self.chips = Chips(100)

    def draw(self, deck):
        self.hand.add_card(deck.draw())

    def show(self):
        print(f"{self.name}'s cards:\n")
        if len(self.hand.cards) > 0:
            for card in self.hand.cards:
                card.show()
        else:
            print("You have no cards at the moment")


class BlackJack:

    def __init__(self):
        print("Welcome to BlackJack")
        # Define the dealer player and the human player
        self.dealer = Player("Dealer")
        self.player = Player(input("Hello player, what is your name : "))
        self.players = [self.dealer, self.player]
        # Play the game
        self.game_over = False

    def show_some(self):
        os.system('clear')
        for player in self.players:
            print(f"{player.name}'s cards:")
            if player.name == "Dealer" and len(player.hand.cards) == 2:
                print(player.hand.cards[0])
                print("##")
            else:
                for card in player.hand.cards:
                    print(card)

    def show(self):
        os.system('clear')
        for player in self.players:
            print(f"{player.name}'s cards:")
            for card in player.hand.cards:
                print(card)

    def ask_players_bet(self):
        while True:
            try:
                bet = int(input(f"{self.player.name}, how much would you like to bet : "))
            except ValueError:
                print("Please input an integer value")
            else:
                if bet <= self.player.chips.value:
                    self.player.chips.bet = bet
                    break
                print(f"Insufficient chips. Available chips : {self.player.chips}.")

    def initial_draw(self, deck: Deck):
        for player in self.players:
            player.hand.cards = []
            player.hand.value = 0
            for _ in range(0, 2):
                player.draw(deck)

    def hit_or_stand(self, deck):
        while True:
            decision = input("Do you want to hit or stand? [h/s] : ")
            if decision[0].lower() not in ["h", "s"]:
                print("Invalid input, valid inputs are h or s")
            else:
                if decision[0].lower() == "h":
                    self.player.draw(deck)
                    self.player.hand.adjust_for_aces()
                break

    def dealer_hit(self, deck: Deck):
        if self.player.hand.value <= 21:
            while self.dealer.hand.value < 17:
                self.dealer.draw(deck)
                self.dealer.hand.adjust_for_aces()

    def tie_game(self):
        print('Dealer and player tie! PUSH!')
        self.game_over = True

    def player_wins(self):
        print(f"{self.player.name} WINS!")
        self.player.chips.win_bet()
        self.game_over = True

    def player_busts(self):
        print(f"{self.player.name} BUST!")
        self.player.chips.lose_bet()
        self.game_over = True

    def dealer_busts(self):
        print(f"{self.dealer.name} BUST!")
        self.player.chips.win_bet()
        self.game_over = True

    def dealer_wins(self):
        print(f"{self.dealer.name} WINS!")
        self.player.chips.lose_bet()
        self.game_over = True

    def win_or_bust(self):
        if self.dealer.hand.value > 21:
            self.dealer_busts()
        elif self.dealer.hand.value > self.player.hand.value:
            self.dealer_wins()
        elif self.dealer.hand.value < self.player.hand.value:
            self.player_wins()
        else:
            self.tie_game()

    def replay(self):
        if self.player.chips.value == 0:
            print("Thank you for playing! You do not have any chips to play further.")
            self.game_over = True
        else:
            while True:
                decision = input("Do you want to play again? [y/n] :")
                if decision[0].lower() not in ["y", "n"]:
                    print("Invalid input, valid options are y or n")
                else:
                    if decision[0].lower() == "y":
                        self.game_over = False
                    else:
                        print("Thank you for playing!")
                    break

    def play(self):
        while True:
            deck = Deck()
            deck.shuffle()
            self.initial_draw(deck)
            self.ask_players_bet()
            self.show_some()
            while not self.game_over:

                # Players turn - hit or stand
                self.hit_or_stand(deck)
                self.show_some()

                # Check if players hand is busted
                if self.player.hand.value > 21:
                    self.player_busts()
                    break

                # If player hasn't busted, play Dealer's hand until Dealer reaches 17
                self.dealer_hit(deck)
                self.show()

                # Run diff win/bust scenarios
                self.win_or_bust()

            # Inform player of their chips
            print(f"\nYour total chips are : {self.player.chips} ")
            # Play again?
            self.replay()
            if self.game_over:
                break


play = BlackJack()
play.play()
