def rock_paper_scissors(symbol_1: str, symbol_2: str) -> str:
    vals = ["rock", "paper", "scissors", "well"]
    if symbol_1 in vals and symbol_2 in vals:
        if symbol_1 == symbol_2:
            return "tie"
    else: return "incorrect input"


def main() -> None:
    # Tests only for student side debugging
    assert rock_paper_scissors("rock", "scissors") == "player_1"
    assert rock_paper_scissors("well", "paper") == "player_2"
    assert rock_paper_scissors("well", "stone") == "incorrect input"


if __name__ == '__main__':
    main()
