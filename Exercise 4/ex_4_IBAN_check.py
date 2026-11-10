# you must not import anything for this task
def verify_iban(iban: str) -> bool:
    n_string = ""
    l_f = ""
    for i, c in enumerate(iban):
        if i <= 3:
            l_f += numberify(c)
        else:
            n_string += numberify(c)
    return int(f"{n_string}{l_f}") % 97 == 1

def numberify(s: str) -> str:
    if s not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        return str(ord(s)-55)
    else: return s

def main() -> None:
    assert verify_iban('GB82WEST12345698765432') is True
    assert verify_iban('DE89370400440532013000') is True
    assert verify_iban('GB82WEST12345698765431') is False


if __name__ == "__main__":
    main()
