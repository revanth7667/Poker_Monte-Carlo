import sys
from future import FutureCards
from pinput import read_input
from deck import build_remaining_deck
from evaluate import compare_hands


def print_results(wins, n):
    for i in range(0, len(wins) - 1):
        print("Hand {} won {} / {} times".format(i, wins[i], n))
        pass
    print("and there were {} ties".format(wins[len(wins) - 1]))
    pass


def monte_carlo(decks):
    win_hand = decks[0]
    win_ind = 0
    tie_flag = False
    for i in range(1, len(decks)):
        ans = compare_hands(win_hand, decks[i])
        if ans < 0:
            win_hand = decks[i]
            win_ind = i
            tie_flag = False
        elif ans == 0:
            tie_flag = True
            pass
        pass
    if tie_flag:
        return len(decks)
    else:
        return win_ind


def main():
    # get count of command line arguments
    argc = len(sys.argv)
    # check user input
    print(sys.argv)
    f_name = sys.argv[1]

    if argc >= 3:
        num_trials = int(sys.argv[2])
    else:
        num_trials = 10000
        pass

    # read from file
    fc = FutureCards()
    decks = read_input(f_name, fc)

    d = build_remaining_deck(decks)
    # do monte carlos
    wins = []
    for i in range(len(decks) + 1):
        wins.append(0)
        pass

    for i in range(num_trials):
        d.shuffle()
        fc.future_cards_from_deck(d)
        ind = monte_carlo(decks)
        wins[ind] = wins[ind] + 1

    # print results
    print_results(wins, num_trials)
    pass


if __name__ == "__main__":
    main()
