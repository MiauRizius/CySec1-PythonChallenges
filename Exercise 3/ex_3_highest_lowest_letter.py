def highest_lowest_letter(s: str) -> tuple[int, int]:
    cur_high, cur_low = -5000, 5000
    for e in s:
        if ord(e) < cur_low: cur_low = ord(e)
        elif ord(e) > cur_high: cur_high = ord(e)
    return (cur_high, cur_low)


def main() -> None:
    assert highest_lowest_letter("Hello World!") == (114, 32)
    assert highest_lowest_letter("AAA") == (65, 65)
    assert highest_lowest_letter(
        "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et "
        "dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet "
        "clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, "
        "consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, "
        "sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, "
        "no sea takimata sanctus est Lorem ipsum dolor sit amet.") == (121, 32)


if __name__ == '__main__':
    main()
