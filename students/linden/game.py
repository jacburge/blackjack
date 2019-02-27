#!/usr/bin/env python3.7

"""
This is the main file of the Blackjack game.  From here, the game
is started, people are added to the game, cards are dealt, wins are
determined, etc.

Based on the rules at:

https://www.bicyclecards.com/how-to-play/blackjack/
"""

import logging  # https://docs.python.org/3/howto/logging.html
from typing import Tuple

import yaml

from common.timeit import timeit_to_log
from deck import Deck
from player import Player

CONFIG_FILE = 'config.yaml'  # TODO pull this in from the commandline

# do this in __init__ so it runs at startup so it is available for all classes after we package it
# creates a global variable logger with your filename
logger = logging.getLogger(__name__)  # pylint: disable=invalid-name


def read_config(CONFIG_FILE: str) -> dict:
    ''' Read in the configuration information from a config file. '''
    # open as read-only with context manager that will close your file for you
    with open(CONFIG_FILE, 'r') as cfg:
        config_data = yaml.load(cfg.read())
    return config_data


def setup_logging(config: dict):
    '''Set up the logging facility for our game. '''
    # if len(sys.argv) > 1 and sys.argv[1 == -'d':
    #     level= logging.DEBUG
    # else:
    #     level= logging.INFO
    # config= Config().data
    logging.basicConfig(filename=config['logFile'], level=config['logLevel'],
                        format=config['logMessageFormat'])


def say(player, text: str) -> None:
    """
    Say something.  As long as we're in console-land, this is just a
    print() statement, but if we decide to move to Slack or irc, it
    gives us a little leg-up.
    """
    logger.debug
    if player:
        localText = '{}: {}'.format(player.name, text)
        logger.debug(localText)
        print(localText)
    else:
        logger.debug(text)
        print(text)


def get_input() -> str:
    """
    Retrieve input from the user.  Like say(), this is present mostly
    for future expansion capability.
    """
    return input()   # stops cursor and waits for terminal input


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
        players.append(Player(name))
        say(players[-1], 'Are there more players to sign up? (y/N)')
        response = get_input()
        if not response:
            keep_going = 'n'
        else:
            keep_going = response
    return players


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
        value = card.value()
        if value == 1:
            aces += 1
            score += 1
        else:
            score += value
    if not aces:
        return score
    for num in range(aces):
        curr_aces = aces - num
        if score + (curr_aces * 10) <= 21:
            score += curr_aces * 10
            return score
    return score


def format_cards(player: Player) -> str:
    """
    Formats the player's current hand.
    """
    str_list = []
    for card in player.all_cards:
        str_list.append(card.rank)
        str_list.append(' of ')
        str_list.append(card.suit)
        str_list.append(', ')
        # str_list.append('{}'.format(card.value()))
        # str_list.append(", ")

    str_list = str_list[:-1]  # remove last 2 chars
    bill = ''.join(str_list)
    # print(bill)
    return bill


def ask_player_position(deck: Deck, players: list) -> None:
    """
    Go through the list of players, and for each of them, ask if they
    want to hit or stay.  Return when all players are finished.
    """
    for player in players:
        say(player, 'Greetings!')
        deal_cards(deck, player, 2)
        say(player, format_cards(player))
        while True:
            report_score(player)
            say(player, 'Would you like to hit or stay? (h/S) ')
            answer = get_input()
            if answer.lower() in ['h', 'hit']:
                deal_cards(deck, player, 1)
                say(player, format_cards(player))
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

@timeit_to_log
def play_game() -> None:
    """
    Start the game.  This is the main event loop.
    """
    # signal.signal(
    #         signal.SIGINT, signal_handler)  # in case someone hit Ctrl_c+or x. Good for DB connections to give them time to close clean, nice.
    # signal.signal(signal.SIGITERM, signal_handler)

    config = read_config(CONFIG_FILE)
    setup_logging(config)
    logger.info('Game starting...')

    say(None, 'Welcome to Blackjack!')
    deck = Deck()  # start with a single deck
    deck.shuffle()
    players: list = get_players()
    dealer: Player = Player('Dealer', is_dealer=True)
    deal_cards(deck, dealer, 2)
    ask_player_position(deck, players)
    # for player in players:
    #     print("Print player.points to get exception: "+str(player.points))

    # TODO: missing features at this point:
    # * betting
    # * comparisons with the dealer's hand


if __name__ == '__main__':
    play_game()
