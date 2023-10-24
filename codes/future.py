from deck import Deck
from card import Card


class FutureCards:
    """Future Cards Class for Poker Game"""

    def __init__(self, future_cards_in=None):
        if future_cards_in == None:
            self.future_cards = []
        else:
            self.future_cards = future_cards_in
        pass

    def __str__(self):
        ans = ""
        for x in self.future_cards:
            ans = ans + str(x) + "\n"
            pass
        return ans

    def __repr__(self):
        ans_rep = "FutureCards:" + "\n"
        for x in range(len(self.future_cards)):
            ans_rep = ans_rep + "?{}: {}".format(x, str(self.future_cards[x])) + "\n"
            pass
        return ans_rep

    def add_future_card(self, ind, c):
        ln = len(self.future_cards)
        if ln < ind + 1:
            for i in range((ind + 1) - ln):
                self.future_cards.append(Deck())
                pass
            pass
        self.future_cards[ind].add_card(c)
        pass

    def future_cards_from_deck(self, d):
        for z in self.future_cards:
            dc = d.draw()
            for x in z.cards:
                x.value = dc.value
                x.suit = dc.suit

                pass
            pass

    pass


if __name__ == "__main__":
    c1 = Card("A", "s")
    c2 = Card()
    c3 = Card("9", "h")
    c4 = Card("8", "c")
    D1 = Deck([c1, c2, c2])
    D2 = Deck([c1, c3, c4, c2])
    D3 = Deck([c1, c3, c4])
    x = FutureCards([D1, D2, D3])
    d3 = Deck([c1, c2, c3])
    print(repr(x))
    x.future_cards_from_deck(d3)
    print(repr(x))

    pass
