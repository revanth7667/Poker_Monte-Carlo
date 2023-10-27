"""
To Call poker.py with default arguments for users who don't want to use command line
"""
import subprocess


def call_poker():
    file_path = "../poker_test.txt"  # modify this as required
    n = 10000  # default number of runs, modify if required

    subprocess.run(["python", "poker.py", file_path, str(n)])

    pass


if __name__ == "__main__":
    call_poker()
