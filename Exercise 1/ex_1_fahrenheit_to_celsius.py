def fahrenheit_to_celsius(f: int) -> float:
    return round((f - 32) / 1.8, 2)


def main() -> None:
    assert fahrenheit_to_celsius(98) == 36.67
    assert fahrenheit_to_celsius(-35) == -37.22
    assert fahrenheit_to_celsius(1337) == 725.0


if __name__ == '__main__':
    main()
