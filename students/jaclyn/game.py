#!/usr/bin/env python3.7

"""
This is the main file of the Blackjack game.  From here, the game
is started, people are added to the game, cards are dealt, wins are
determined, etc.

Based on the rules at:

https://www.bicyclecards.com/how-to-play/blackjack/
"""
import logging
import yaml
from deck import Deck
from player import Player

# pylint: disable=fixme

logger = logging.getLogger('blackjack') # pylint: disable=invalid-name
CONFIG_FILE = 'config.yaml'

def read_config(filename: str) -> dict:
    """ Read in the configuration information from the config file. """
    with open(filename, 'r') as fpth:
        config_data = yaml.load(fpth.read())
    return config_data

def setup_logging(config: dict) -> None:
    """ Set up the logging facility for our game. """
    logfile = config['logfile']
    loglevel = config['loglevel']
    logformat = config['format']
    logging.basicConfig(filename=logfile,
                        level=loglevel,
                        format=logformat)

def say(player: Player, text: str) -> None:
    """
    Say something.  As long as we're in console-land, this is just a
    print() statement, but if we decide to move to Slack or irc, it
    gives us a little leg-up.

    Note that 'player' can either be None or a Player. Remember that
    a None type doesn't have a .name attribute, so you'll need to
    handle the two strings differently
    """
    if player:
        msg = '{}: {}'.format(player.name, text)
    else:
        msg = text
    print(msg)
    logger.debug(msg)

def get_input() -> str:
    """
    Retrieve input from the user.  Like say(), this is present mostly
    for future expansion capability.
    """
    return input()

def get_players() -> list:
    """
    Get a list of players on the console.  We assume that the computer
    is the dealer, so all players will be non-dealer players.
    """
    players = []
    keep_going = 'y'
    while keep_going.lower() not in ['n', 'no']:
        say(None, 'Please enter your name: ')
        name = get_input()
        players.append(initialize_player(name))
        say(players[-1], 'Are there more players to sign up? (y/N)') #default no
        response = get_input()
        if not response:
            keep_going = 'n'
        else:
            keep_going = response
    return players

def initialize_player(name: str, money: float = 10) -> Player:
    """ Set up the player with a Player object and an initial amount of money.
    """
    player = Player(name)
    player.wallet.add_money(money)
    return player

def deal_cards(deck: Deck, player: Player, num: int) -> None:
    """
    Deal the specified number of cards to the specified player, from
    the given deck.
    """
    for _ in range(num):
        card = deck.deal()
        player.add_card(card)

def report_score(player: Player) -> int:
    """
    Tell the player what their current score is, and return that score
    to the caller.
    """
    score = get_score(player)
    say(player, 'You have {} points'.format(score))
    return score

def get_score(player: Player) -> int:
    """
    Determine the number of points the player currently has and return
    it.  Each ace comes in as 1 point initially.  Track the number of
    aces in the hand, and test adding each in turn, adding 10 to the
    score for each until the score goes over 21, then stop adding 10
    for each ace.
    """
    aces = 0
    score = 0
    for card in player.all_cards:
        points = card.points
        if points == 1:
            aces += 1
            score += 1
        else:
            score += points
    if not aces:
        return score
    for num in range(aces):
        curr_aces = aces - num
        if score + (curr_aces * 10) <= 21:
            score += curr_aces * 10
            return score
    return score

def print_cards(player: Player) -> None:
    """
    Print out the player's current hand.
    """
    # TODO: the card format is not very nice, figure out why Card's
    # __str__ method isn't getting called like expected
    cards = player.all_cards
    clean_cards = [str(card) for card in cards]
    say(player, 'Your hand: {}'.format(clean_cards))
    return '{}: Your hand: {}'.format(player.name, clean_cards)

def get_bet_amount(player: Player) -> float:
    while True:
        bet_amount = get_input()
        try:
            bet_amount = float(bet_amount)
            return bet_amount
        except ValueError:
            say(player, f'{bet_amount} is not a number, try again')

def ask_player_position(deck: Deck, players: list) -> None:
    """
    Go through the list of players, and for each of them, ask if they
    want to hit or stay.  Return when all players are finished.
    """
    for player in players:
        say(player, 'Greetings!')
        deal_cards(deck, player, 2)
        say(player, f'You have ${player.wallet.balance}, what is your bet?')
        bet_amount = get_bet_amount(player)
        player.wallet.remove_money(float(bet_amount))
        say(player, get_cards(player))
        while True:
            report_score(player)
            say(player, 'Would you like to hit or stay? (h/S) ')
            answer = get_input()
            if answer.lower() in ['h', 'hit']:
                deal_cards(deck, player, 1)
                print_cards(player)
                if get_score(player) >= 21:
                    break
            else:
                break
        score = report_score(player)
        # TODO: this takes no account of the dealer's cards, add code
        # to check the dealer's hand
        if score == 21:
            say(player, 'Blackjack!')

        if score >= 21:
            say(player, 'Bust!  Too bad.')

def play_game() -> None:
    """
    Start the game.  This is the main event loop.
    """
    config = read_config(CONFIG_FILE)
    setup_logging(config)
    logger.info('Game starting')
    say(None, 'Welcome to Blackjack!')
    deck: Deck = Deck() # start with a single deck
    deck.shuffle()
    players: list = get_players()
    dealer: Player = Player('Dealer', is_dealer=True)
    dealer.wallet.add_money(1000)
    deal_cards(deck, dealer, 2)
    ask_player_position(deck, players)
    # TODO: missing features at this point:
    # * betting
    # * comparisons with the dealer's hand


if __name__ == '__main__':
    play_game()
