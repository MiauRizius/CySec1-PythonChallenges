def insert_string(original_string: str, loc: int, to_insert: str) -> str:
    if len(original_string) == 0:
        return to_insert
    else:
        return original_string.replace(original_string[loc-1], to_insert+original_string[::loc])


def main() -> None:
    print(insert_string("Hello rld!", 6, "Wo"))
    print(insert_string("", 0, "Test"))
    print(insert_string("Cy", 2, "Sec"))

    assert insert_string("Hello rld!", 6, "Wo") == "Hello World!"
    assert insert_string("", 0, "Test") == "Test"
    assert insert_string("Cy", 2, "Sec") == "CySec"


if __name__ == '__main__':
    main()
