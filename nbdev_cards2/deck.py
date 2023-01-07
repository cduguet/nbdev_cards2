# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_deck.ipynb.

# %% auto 0
__all__ = ['Deck', 'draw_n']

# %% ../nbs/01_deck.ipynb 3
from fastcore.utils import *
from .card import *
import random

# %% ../nbs/01_deck.ipynb 4
class Deck:
    "A deck of 52 cards, not including jokers"
    def __init__(self):
        self.cards = [Card(s,r) for s in range(4) for r in range(1,14)]
        self.n = len(self.cards)
    def __len__(self): return len(self.cards)
    def __str__(self): return "; ".join(map(str, self.cards))
    __repr__ = __str__
    def __contains__(self, c): return c in self.cards
    def shuffle(self):
        "Shuffle the cards in this deck"
        random.shuffle(self.cards)

# %% ../nbs/01_deck.ipynb 13
def draw_n(n:int, # Number of cards to draw
           replace:bool=True): # Whether to replace cards after drawing
    "Draw `n` cards from the deck"
    d = Deck()
    d.shuffle()
    if replace: return[d.cards[random.choice(range(len(d.cards)))] for _ in range(n)]
    else: return d.carsd[:n]
