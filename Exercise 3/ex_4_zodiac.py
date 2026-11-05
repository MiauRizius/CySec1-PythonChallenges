def zodiac(birth_year: int) -> str:
    zod: dict[int, str] = {
        1924: "Rat",
        1925: "Ox",
        1926: "Tiger",
        1927: "Rabbit",
        1928: "Dragon",
        1929: "Snake",
        1930: "Horse",
        1931: "Goat",
        1932: "Monkey",
        1933: "Rooster",
        1934: "Dog",
        1935: "Pig"
    }
    year = birth_year
    while year not in zod:
        year -= 12
    return zod[year]


def main() -> None:
    # Tests for student side debugging only
    assert zodiac(2023) == "Rabbit"
    assert zodiac(2002) == "Horse"


if __name__ == '__main__':
    main()
