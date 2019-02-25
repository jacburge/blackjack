#!/usr/bin/env python3.7

"""
This is the main file of the Blackjack game.  From here, the game
is started, people are added to the game, cards are dealt, wins are
determined, etc.

Based on the rules at:

https://www.bicyclecards.com/how-to-play/blackjack/
"""

from deck import Deck
from player import Player

def say(player: Player, text: str) -> None:
    """
    Say something.  As long as we're in console-land, this is just a
    print() statement, but if we decide to move to Slack or irc, it
    gives us a little leg-up.
    """
    if player:
        print('{}: {}'.format(player.name, text))
    else:
        print(text)


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
    for card in player.all_cards():
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


def print_cards(player: Player) -> None:
    """
    Print out the player's current hand.
    """
    # TODO: the card format is not very nice, figure out why Card's
    # __str__ method isn't getting called like expected
    cards = player.all_cards()
    say(player, 'Your hand: {}'.format(cards))


def ask_player_position(deck: Deck, players: list) -> None:
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
    say(None, 'Welcome to Blackjack!')
    deck: Deck = Deck() # start with a single deck
    deck.shuffle()
    players: list = get_players()
    dealer: Player = Player('Dealer', is_dealer=True)
    deal_cards(deck, dealer, 2)
    ask_player_position(deck, players)
    # TODO: missing features at this point:
    # * betting
    # * comparisons with the dealer's hand


if __name__ == '__main__':
    play_game()
