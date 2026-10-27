def rec_factorial(x: int) -> int:
    return x*rec_factorial(x-1) if x > 1 else 1


def main() -> None:
    # Tests only for student side debugging
    assert rec_factorial(2) == 2
    assert rec_factorial(5) == 120


if __name__ == '__main__':
    main()
