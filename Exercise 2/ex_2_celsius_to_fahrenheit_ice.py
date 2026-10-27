def celsius_to_fahrenheit_ice(celsius: int) -> str:
    fahr = round((celsius * 1.8) + 32, 2)
    return f"H2O is {'solid' if fahr <= 32 else ('liquid' if fahr < 212 else 'gas')} at {fahr}f"


def main() -> None:
    # Tests only for student side debugging
    assert celsius_to_fahrenheit_ice(-12) == "H2O is solid at 10.4f"
    assert celsius_to_fahrenheit_ice(32) == "H2O is liquid at 89.6f"
    assert celsius_to_fahrenheit_ice(112) == "H2O is gas at 233.6f"


if __name__ == '__main__':
    main()
