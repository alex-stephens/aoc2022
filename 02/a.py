MOVES = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}
PLAYER_SCORE = {"Rock": 1, "Paper": 2, "Scissors": 3}
OUTCOME_SCORE = {"Win": 6, "Lose": 0, "Draw": 3}


def compute_result(m1, m2):

    m1, m2 = MOVES[m1], MOVES[m2]
    if m1 == m2:
        outcome = "Draw"
    elif m1 == "Rock" and m2 == "Scissors":
        outcome = "Win"
    elif m1 == "Paper" and m2 == "Rock":
        outcome = "Win"
    elif m1 == "Scissors" and m2 == "Paper":
        outcome = "Win"
    else:
        outcome = "Lose"

    return PLAYER_SCORE[m1] + OUTCOME_SCORE[outcome]


def main():
    filename = "input.txt"
    result = 0

    with open(filename) as f:
        for line in f.readlines():
            # m2 is the opponent's move
            m2, m1 = line.strip().split(" ")

            s = compute_result(m1, m2)
            result += s
    print(result)


if __name__ == "__main__":
    main()
