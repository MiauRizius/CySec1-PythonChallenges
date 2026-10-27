def find_first_occurrence(haystack: str, needle: str) -> int | bool:
    if needle == "": return 0
    for i in range(1, len(haystack)+1):
        print(haystack[i:][:len(needle)])
        if haystack[i:][:len(needle)] == needle:
            return i
    return False


def main() -> None:
    print(find_first_occurrence("DXcXpSUjwBLZSIKMU", ""))


if __name__ == '__main__':
    main()