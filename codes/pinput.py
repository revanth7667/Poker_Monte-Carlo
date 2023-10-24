from deck import Deck
from card import Card
from future import FutureCards


def hand_from_string(s, fc):
    out = Deck()
    lst = s.split()

    for aa in lst:
        if aa[0] == "?":
            pcc = Card("?", "?")
            out.add_card(pcc)
            fc.add_future_card(int(aa[1:]), pcc)
        else:
            out.add_card(Card(aa[0], aa[1]))
            pass
        pass
    return out


def read_input(file, fc):
    decks = []
    with open(file) as yy:
        for line in yy:
            decks.append(hand_from_string(line, fc))
            pass
        pass
    return decks


if __name__ == "__main__":
    zz = FutureCards()
    print(repr(zz))
    print(read_input("test.txt", zz))
    # print(hand_from_string("Js   2c   Qc Ah 2d 7s 3c 5s",zz))
    # print(hand_from_string("Ac ?1 ?12 8h",zz))
    print(repr(zz))

    with open("test.txt") as bb:
        for cc in bb:
            print(cc.split())
            pass
        pass
    pass
