# I don't know if I am supposed to do it like this, but I don't find any other solution. But hey, it works :)
def insert_string(original_string: str, loc: int, to_insert: str) -> str:
    if len(original_string) == 0:
        return to_insert
    elif len(original_string) > loc:
        return original_string[:loc] + to_insert + original_string[loc:]
    else:
        return original_string + to_insert


def main() -> None:
    assert insert_string("Hello rld!", 6, "Wo") == "Hello World!"
    assert insert_string("", 0, "Test") == "Test"
    assert insert_string("Cy", 2, "Sec") == "CySec"


if __name__ == '__main__':
    main()
