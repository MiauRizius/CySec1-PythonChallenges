def reverse_words(s: str) -> str:
    l = s.split(" ")
    s = ""
    for i, e in enumerate(l):
        s += f"{l[-(i+1)]}{"" if i+1 == len(l) else " "}"
    return s


def main() -> None:
    print(reverse_words("World! Hello"))
    assert reverse_words("World! Hello") == "Hello World!"
    assert reverse_words("This is a test") == "test a is This"
    assert reverse_words("Cysec ") == " Cysec"


if __name__ == '__main__':
    main()
