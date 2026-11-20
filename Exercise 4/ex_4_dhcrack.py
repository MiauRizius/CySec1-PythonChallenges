def crack_dh_exchange(p: int, g: int, A: int, B: int) -> int:
    idx, current_val = 0, 1
    while current_val != A and current_val != B:
        current_val = (current_val * g) % p # should be even faster than pow i guess?
        idx += 1
    return pow(A, idx, p) if current_val == B else pow(B, idx, p)

def main() -> None:
    # Tests for student side debugging only
    assert crack_dh_exchange(613, 560, 217, 150) == 285
    assert crack_dh_exchange(941, 101, 335, 500) == 608


if __name__ == '__main__':
    main()
