import math

def compute_birthday_paradox(n: int) -> float:
    if n < 2:
        raise ValueError("n too small")
    elif n > 120:
        raise ValueError("n too large")
    else:
        return round( 1 - (math.factorial(365) / (math.factorial(365 - n) * 365**n)), 4)


if __name__ == '__main__':
    print(compute_birthday_paradox(23))
    assert compute_birthday_paradox(23) == 0.5073
    try:
        compute_birthday_paradox(1)
        assert False  # should not reach here
    except ValueError as e:
        assert str(e) == 'n too small'
    except Exception:
        assert False

    try:
        compute_birthday_paradox(121)
        assert False  # should not reach here
    except ValueError as e:
        assert str(e) == 'n too large'
    except Exception:
        assert False
