from card import Card, card_from_num
import random


class Deck:
    """Deck Class for Poker Game"""

    def __init__(self, cards_in=None):
        if cards_in == None:
            self.cards = []
        else:
            self.cards = cards_in
        pass

    def __str__(self):
        out_str = ""
        for x in self.cards:
            out_str = out_str + str(x) + " "
            pass
        return out_str[:-1]

    def __repr__(self):
        out_str = "Deck("
        for x in self.cards:
            out_str = out_str + str(x) + " "
            pass
        return out_str[:-1] + ")"
        pass

    def add_card(self, c):
        self.cards.append(c)
        pass

    def add_placeholder_card(self):
        place_card = Card()
        self.cards.append(place_card)
        return place_card

    def contains(self, c):
        for x in self.cards:
            if x == c:
                return True
            pass
        return False

    def shuffle(self):
        random.shuffle(self.cards)
        pass

    def assert_full(self):
        ans = True
        for i in range(52):
            if not (self.contains(card_from_num(i))):
                ans = False
                pass
            pass
        ans = ans and len(self.cards) == 52
        assert ans
        pass

    # takes card from from deck, appends it to end, and returns it
    def draw(self):
        x = self.cards.pop(0)
        self.cards.append(x)
        return x
        pass

    # sorts high to low
    def sort(self):
        self.cards = sorted(self.cards, reverse=True)
        pass

    pass


# builds and returns complete deck except for cards in hands
def build_remaining_deck(hands):
    ans = []
    for i in range(52):
        card_test = card_from_num(i)
        required = True
        for x in hands:
            if x.contains(card_test):
                required = False
                pass
            pass
        if required:
            ans.append(card_test)
            pass
        pass
    return Deck(ans)


if __name__ == "__main__":
    card_1 = Card("A", "s")
    card_2 = Card("9", "c")
    card_3 = Card("7", "h")
    deck_1 = Deck([card_1, card_2])
    print(deck_1.contains(card_2))
