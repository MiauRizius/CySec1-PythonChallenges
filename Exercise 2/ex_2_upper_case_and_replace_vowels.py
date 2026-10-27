# Write a python function called upper_case_and_replace_vowels that converts its input string to uppercase and replaces all vowels from it with "x".

def upper_case_and_replace_vowels(my_string: str) -> str:
    s = ""
    vowels = ["A", "E", "I", "O", "U"]
    for el in my_string.upper():
        if el in vowels: el = "x"
        s += el
    return s


def main() -> None:
    # Tests for upper_case_and_replace_vowels function
    assert upper_case_and_replace_vowels("hello world") == "HxLLx WxRLD"
    assert upper_case_and_replace_vowels("aEu") == "xxx"


if __name__ == '__main__':
    main()
