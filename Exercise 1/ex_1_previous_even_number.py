def previous_even_number(n: int) -> int:
    return n - (2 - (n % 2))


def main() -> None:
    assert previous_even_number(6) == 4
    assert previous_even_number(81) == 80
    assert previous_even_number(-41) == -42


if __name__ == '__main__':
    main()
