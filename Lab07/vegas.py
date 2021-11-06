'''
author: Gavin Harrold gsh3009@rit.edu
file: vegas.py
language: python3
using a random deck of cards, attempts to place all cards in ascending order in the victory pile using discard piles
'''


import cs_stack
import cs_queue
import random

def init_deck(size):
    '''
    creates deck of cards of length size using a queue
    :return: deck of cards as queue
    '''
    deck = cs_queue.make_empty_queue()

    for i in range(size):
        cs_queue.enqueue(deck, i+1)
    return deck

def random_draw(deck):
    '''
    deals a randomly selected card and removes it from the deck
    :param deck: queue representing a deck of cards
    :return: randomly selected card
    '''
    shuffles = random.randint(0, deck.size-1)
    for i in range(shuffles):
        cs_queue.enqueue(deck, cs_queue.dequeue(deck))

    return cs_queue.dequeue(deck)

def play_game(deck):
    '''
    deals each card out using random_draw and keeps going until all cards are dealt
    pulls top card from discard stacks if the top is the card being searched for
    removes from stack afterwards
    :param deck: queue representing deck of cards
    :return:
    '''
    discard1 = cs_stack.make_empty_stack()
    discard2 = cs_stack.make_empty_stack()
    victoryPile = cs_stack.make_empty_stack()
    targetCard = 1
    notOver = True
    while notOver:
        while True:
            takeFromDiscard = False
            if not cs_stack.is_empty(discard1):
                if cs_stack.top(discard1) == targetCard:
                    cs_stack.push(victoryPile, cs_stack.top(discard1))
                    cs_stack.pop(discard1)
                    targetCard += 1
                    takeFromDiscard = True
            if not cs_stack.is_empty(discard2):
                if cs_stack.top(discard2) == targetCard:
                    cs_stack.push(victoryPile, cs_stack.top(discard2))
                    cs_stack.pop(discard2)
                    targetCard += 1
                    takeFromDiscard = True
            if not takeFromDiscard:
                break

        if not cs_queue.is_empty(deck):
            currentCard = random_draw(deck)
            if currentCard == targetCard:
                cs_stack.push(victoryPile, currentCard)
                targetCard += 1
                continue
            if cs_stack.is_empty(discard1):
                cs_stack.push(discard1, currentCard)
            elif currentCard < cs_stack.top(discard1):
                cs_stack.push(discard1, currentCard)
            else:
                cs_stack.push(discard2, currentCard)
        else:
            notOver = takeFromDiscard

    return victoryPile.size

def main():
    '''
    takes user input for deck size and creates deck before running game
    prints average win pile size as well as the minimum victory and maximum victory
    '''
    userSize = int(input("Enter a deck size: "))
    gamesToPlay = int(input("How many games will be played with this deck size? "))
    gamesToPlayOriginal = gamesToPlay
    minWin = userSize
    maxWin = 0
    sum = 0

    while gamesToPlay > 0:
        deck = init_deck(userSize)
        victory = play_game(deck)
        if victory < minWin:
            minWin = victory
        if victory > maxWin:
            maxWin = victory
        sum += victory
        gamesToPlay -= 1

    print("Average victory pile size:", sum/gamesToPlayOriginal)
    print("Max victory pile size:", maxWin)
    print("Minimum victory pile size:", minWin)

if __name__ == '__main__':
    main()