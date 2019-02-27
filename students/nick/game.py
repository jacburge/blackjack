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

LOG = logging.getLogger(__name__)

_CONFIG_FILE = 'config.yaml'

def read_config(filename: str) -> dict:
    """ Read the configuration from the config file """
    # pylint: disable=invalid-name
    with open(filename, 'r') as fp:
        config_data = yaml.load(fp.read())
    return config_data

def setup_logging(config: dict) -> None:
    """ Set up logging with the options specified in the config file """
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
    """
    log = '{}: {}'.format(player.name, text) if player else text
    print(log)
    LOG.debug(log)


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
    say(player, 'Your hand: {}'.format(player.all_cards_printable()))


def ask_player_position(deck: Deck, players: list, dealer: Player) -> None:
    """
    Go through the list of players, and for each of them, ask if they
    want to hit or stay.  Return when all players are finished.
    """
    for player in players:
        say(player, 'Greetings!')
        deal_cards(deck, player, 2)
        print_cards(player)
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
        # player_score = report_score(player)
        dealer_score = report_score(dealer)
        print(dealer_score)
        # if player_score == 21 and dealer_score != 21:
        #     say(player, 'Blackjack!')
        # elif player_score > 21 and dealer_score <= 21:
        #     say(player, 'Bust!  Too bad.')
        # elif player_score < 21 and dealer_score < 21:
        #     if player_score > dealer_score:
        #         say(player, 'Wins!')


def play_game() -> None:
    """
    Start the game.  This is the main event loop.
    """
    setup_logging(read_config(_CONFIG_FILE))
    LOG.info("Welcome to Blackjack!")
    deck: Deck = Deck() # start with a single deck
    deck.shuffle()
    players: list = get_players()
    dealer: Player = Player('Dealer', is_dealer=True)
    deal_cards(deck, dealer, 2)
    ask_player_position(deck, players, dealer)
    # TODO: missing features at this point:
    # * betting
    # * comparisons with the dealer's hand


if __name__ == '__main__':
    play_game()
