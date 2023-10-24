from card import Card, card_from_num, ACE, KING, QUEEN, JACK
from deck import Deck


# finds flush suit
def find_flush(hand):
    s_dict = {"c": 0, "d": 0, "h": 0, "s": 0, "?": 0}
    for h_card in hand.cards:
        x = h_card.suit
        s_dict[x] = s_dict[x] + 1
        pass
    max_val = max(s_dict.values())
    if max_val < 5:
        return None
    else:
        return max(s_dict, key=s_dict.get)
    pass


# makes dictionary of cards values to count of their occurances
def count_values(hand):
    base_dict = {
        14: 0,
        13: 0,
        12: 0,
        11: 0,
        10: 0,
        9: 0,
        8: 0,
        7: 0,
        6: 0,
        5: 0,
        4: 0,
        3: 0,
        2: 0,
    }
    for x in hand.cards:
        base_dict[x.value] = base_dict[x.value] + 1
        pass
    return base_dict


# uses counts dict and returns a tuple (value with most n of a kind, n)
def get_max_count(hand, counts):
    max_count = max(counts.values())
    vals = list(counts.keys())
    vals.sort(reverse=True)
    for i in vals:
        if counts[i] == max_count:
            return (i, counts[i])
        pass
    pass


# finds index of second pair or returns -1 for no sec pair
def find_secondary_pair(hand, counts, val):
    out = -1
    max_2 = sorted(counts.values(), reverse=True)[1]
    if max_2 < 2:
        return out
    else:
        vals = list(counts.keys())
        vals.sort(reverse=True)
        for i in vals:
            if counts[i] == max_2:
                for x in range(len(hand.cards)):
                    if (hand.cards[x].value == i) and (i != val):
                        return x
                    pass
                pass
            pass
        pass
    pass


# get first index of value in hand
def get_kind_index(hand, value):
    for i in range(len(hand.cards)):
        if hand.cards[i].value == value:
            return i
        pass


# build hand with n of a kind starting at ind
def build_of_a_kind(hand, n, ind):
    in_cards = hand.cards.copy()
    # values_dict = count_values(hand)
    out_list = []
    for i in range(n):
        out_list.append(in_cards.pop(ind))
        pass
    # add remaining cards to deck
    for i in range(5 - n):
        out_list.append(in_cards.pop(0))
        pass
    return Deck(out_list)


# adds secondary pair (for full house or two pair)
def add_pair(hand, pi, ans, ai):
    in_cards = hand.cards.copy()
    out_list = ans.cards.copy()
    if ai == 3:
        out_list[3] = in_cards.pop(pi)
        out_list[4] = in_cards.pop(pi)
    else:
        out_list[2] = in_cards.pop(pi)
        out_list[3] = in_cards.pop(pi)
        for x in in_cards:
            if x not in out_list:
                out_list[4] = x
                break
            pass
        pass
    return Deck(out_list)


# helper for is_straight_at
def is_n_length_straight_at(hand, ind, fs, n):
    act_len = 1
    r_fs = "cdhs"
    if fs != None:
        r_fs = fs
        pass
    prev_card = hand.cards[ind]
    if prev_card.suit not in r_fs:
        return False

    for i in range(ind + 1, len(hand.cards)):
        current_card = hand.cards[i]
        if current_card.value == prev_card.value - 1:
            if current_card.suit in r_fs:
                act_len = act_len + 1
                if act_len == n:
                    return True
                prev_card = current_card
                pass
        elif current_card.value == prev_card.value:
            pass
        else:
            return False
        pass
    if act_len == n:
        return True
    else:
        return False
    pass


# helper for is_straight_at
def is_ace_low_straight_at(hand, ind, fs):
    ace_present = False
    r_fs = "cdhs"
    if fs != None:
        r_fs = fs
        pass

    # we need to have ace and of same suit if applicable
    # for x in hand.cards:
    x = hand.cards[ind]
    if (x.value == 14) and (x.suit in r_fs):
        ace_present = True
        pass
        # pass
    if not ace_present:
        return False

    # check if ace low straigth present at given position
    for i in range(ind + 1, len(hand.cards)):
        if hand.cards[i].value == 5 and is_n_length_straight_at(hand, i, fs, 4):
            return True
        pass
    return False
    pass


# if fs = None, look for any straight
# if fs = suit, look for straight in suit
# returns -1 for ace-low, 1 for straight, 0 for no straight
def is_straight_at(hand, ind, fs):
    # check first for normal straight
    if is_n_length_straight_at(hand, ind, fs, 5):
        return 1  # since normal straight is present
    elif is_ace_low_straight_at(hand, ind, fs):
        return -1  # since ace low straight present
    else:
        return 0  # no straight present
    pass


# provided
def copy_straight(hand, ind, fs, ace_low=False):
    ans = Deck()
    last_card = None
    target_len = 5
    assert not fs or hand.cards[ind].suit == fs
    if ace_low:
        assert hand.cards[ind].value == ACE
        last_card = hand.cards[ind]
        target_len = 4
        to_find = 5
        ind += 1
        pass
    else:
        # regular straight
        to_find = hand.cards[ind].value
        pass
    while len(ans.cards) < target_len:
        assert ind < len(hand.cards)
        if hand.cards[ind].value == to_find:
            if not fs or hand.cards[ind].suit == fs:
                ans.add_card(hand.cards[ind])
                to_find -= 1
                pass
            pass
        ind += 1
        pass
    if last_card is not None:
        ans.add_card(last_card)
        pass
    assert len(ans.cards) == 5
    return ans


# provided
# looks for a straight (or straight flush if fs is not None)
# calls the student's is_straight_at for each index
# if found, copy_straight returns cards used for straight
def find_straight(hand, fs):
    for i in range(0, len(hand.cards) - 4):
        is_straight = is_straight_at(hand, i, fs)
        if is_straight == 1:
            # straight
            return copy_straight(hand, i, fs)
        pass
    for i in range(0, len(hand.cards) - 4):
        is_straight = is_straight_at(hand, i, fs)
        if is_straight == -1:
            # ace-low straight
            return copy_straight(hand, i, fs, True)
        pass
    return None


# provided
# builds hand with flush suit fs
def build_flush(hand, fs):
    ans = Deck()
    i = 0
    while len(ans.cards) < 5:
        assert i < len(hand.cards)
        if hand.cards[i].suit == fs:
            ans.add_card(hand.cards[i])
            pass
        i += 1
        pass
    return ans


# provided
def evaluate_hand(hand):
    # straight flush
    fs = find_flush(hand)
    straight = find_straight(hand, fs)
    if fs and straight:
        return straight, "straight flush"
    # four of a kind
    val_counts = count_values(hand)
    v, n = get_max_count(hand, val_counts)
    assert n <= 4
    ind = get_kind_index(hand, v)
    if n == 4:
        return build_of_a_kind(hand, 4, ind), "four of a kind"
    # full house
    sec_pair = find_secondary_pair(hand, val_counts, v)
    if n == 3 and sec_pair >= 0:
        ans = build_of_a_kind(hand, 3, ind)
        ans = add_pair(hand, sec_pair, ans, 3)
        return ans, "full house"
    # flush
    if fs:
        return build_flush(hand, fs), "flush"
    # straight
    if straight:
        return straight, "straight"
    # three of a kind
    if n == 3:
        return build_of_a_kind(hand, 3, ind), "three of a kind"
    # two pair
    if n == 2 and sec_pair >= 0:
        ans = build_of_a_kind(hand, 2, ind)
        ans = add_pair(hand, sec_pair, ans, 2)
        return ans, "two pair"
    # pair
    if n == 2:
        return build_of_a_kind(hand, 2, ind), "pair"
    # high card
    ans = Deck()
    ans.cards = hand.cards[0:5]
    return ans, "high card"


def num_from_rank(r):
    ranks = [
        "high card",
        "pair",
        "two pair",
        "three of a kind",
        "straight",
        "flush",
        "full house",
        "four of a kind",
        "straight flush",
    ]
    return ranks.index(r)


# returns positive if hand1 > hand2,
# 0 for tie, or
# negative for hand2 > hand 1
def compare_hands(hand1, hand2):
    hand1.sort()
    hand2.sort()
    val_1 = evaluate_hand(hand1)
    val_2 = evaluate_hand(hand2)
    out = num_from_rank(val_1[1]) - num_from_rank(val_2[1])
    if out == 0:
        for x in range(5):
            out = val_1[0].cards[x].value - val_2[0].cards[x].value
            if out != 0:
                break
            pass
        pass
    return out


if __name__ == "__main__":
    c1_1 = Card("A", "d")
    c2_1 = Card("Q", "h")
    c3_1 = Card("Q", "d")
    c4_1 = Card("J", "h")
    c5_1 = Card("0", "c")
    c6_1 = Card("A", "d")
    c7_1 = Card("4", "c")

    c1_2 = Card("A", "d")
    c2_2 = Card("7", "h")
    c3_2 = Card("5", "d")
    c4_2 = Card("4", "h")
    c5_2 = Card("3", "d")
    c6_2 = Card("2", "d")
    c7_2 = Card("2", "c")

    d1 = Deck([c1_1, c2_1, c3_1, c4_1, c5_1, c6_1, c7_1])
    d2 = Deck([c1_2, c2_2, c3_2, c4_2, c5_2, c6_2, c7_2])

    # d1.sort()
    # d2.sort()
    # print(evaluate_hand(d1))
    # print(d2)
    # print(evaluate_hand(d2))
    print(compare_hands(d1, d2))
    # print(is_n_length_straight_at(d1,0,None,5))
    pass
