import numbers

ACE = 14
KING = 13
QUEEN = 12
JACK = 11


def value_from_letter(let):
    let_dict = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "0": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2,
        "?": 0,
    }

    return let_dict[let]


def check_suit(let):
    suit_val = {"c": 0, "d": 1, "h": 2, "s": 3}
    return suit_val[let]
    pass


def letter_from_value(val):
    val_dict = {
        14: "A",
        13: "K",
        12: "Q",
        11: "J",
        10: "0",
        9: "9",
        8: "8",
        7: "7",
        6: "6",
        5: "5",
        4: "4",
        3: "3",
        2: "2",
        0: "?",
    }

    return val_dict[val]


class Card:
    """Card Class for Poker"""

    def __init__(self, value_in="?", suit_in="?"):
        if value_in == "?" or suit_in == "?":
            if value_in != suit_in:
                raise ValueError("Please Enter a Valid Input")
            pass

        if len(value_in) != 1 or not (value_in in "AKQJ098765432?"):
            raise ValueError("Please Enter Valid Card Value")
        else:
            self.value = value_from_letter(value_in)
            pass
        if len(value_in) != 1 or not (suit_in in "s**h**d**c**?"):
            raise ValueError("Please Enter Valid Suit Value")
        else:
            self.suit = suit_in
            pass

    def __str__(self):
        return "{}{}".format(letter_from_value(self.value), self.suit)
        pass

    def __repr__(self):
        return "Card({}{})".format(letter_from_value(self.value), self.suit)
        pass

    def __eq__(self, other):
        return (self.value == other.value) and (self.suit == other.suit)
        pass

    def __lt__(self, other):
        if self.value < other.value:
            return True
        elif self.value == other.value:
            return check_suit(self.suit) < check_suit(other.suit)
        else:
            return False
        pass

    def is_known(self):
        if self.value == 0 or self.suit == "?":
            return False
        else:
            return True

    pass


def card_from_num(num):
    if not (isinstance(num, int) and (num >= 0 and num <= 51)):
        raise ValueError("Please Enter an integer between 0-51")
    suit_map = {0: "c", 1: "d", 2: "h", 3: "s"}
    suit_value = suit_map[num // 13]
    value_letter = letter_from_value(num % 13 + 2)
    output = Card(value_letter, suit_value)
    output.is_known()
    return output


if __name__ == "__main__":
    print(Card("2", "h"))
