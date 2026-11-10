# you must not import anything for this task
def verify_iban(iban: str) -> bool:
    # TODO implement
    pass


def main() -> None:
    assert verify_iban('GB82WEST12345698765432') is True
    assert verify_iban('DE89370400440532013000') is True
    assert verify_iban('GB82WEST12345698765431') is False


if __name__ == "__main__":
    main()
