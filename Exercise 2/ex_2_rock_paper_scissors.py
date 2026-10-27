def rock_paper_scissors(symbol_1: str, symbol_2: str) -> str:
    vals = ["rock", "paper", "scissors", "well"]
    if symbol_1 in vals and symbol_2 in vals:
        if symbol_1 == symbol_2:
            return "tie"
        elif symbol_2 in slays_what(symbol_1):
            return "player_1"
        else: return "player_2"
    else: return "incorrect input"


def slays_what(str_1):
    if str_1 == "rock":
        return ["scissors"]
    elif str_1 == "paper":
        return ["rock", "well"]
    elif str_1 == "scissors":
        return ["paper"]
    elif str_1 == "well":
        return ["rock", "scissors"]


def main() -> None:
    # Tests only for student side debugging
    assert rock_paper_scissors("rock", "scissors") == "player_1"
    assert rock_paper_scissors("well", "paper") == "player_2"
    assert rock_paper_scissors("well", "stone") == "incorrect input"


if __name__ == '__main__':
    main()
