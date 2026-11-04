def replacement_cipher(key_dict: dict[str, str], cipher_text: str) -> str:
    p = ""
    for e in cipher_text:
        if e in key_dict: p += key_dict[e]
        else: p += e
    return p


def main() -> None:
    # Tests for student side debugging only
    assert replacement_cipher({"e": "c", "g": "a", "d": "f", "v": "e", "r": "b"}, "egdv rgrv") == "cafe babe"


if __name__ == '__main__':
    main()
