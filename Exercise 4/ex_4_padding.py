def compute_pad(message: str) -> str:
    length_pad = bin((len(message)) % (2**8))[2:].rjust(8, "0")
    pad = "1"
    more_pad = 128 - 8 - (len(message) * 8) % 128 - 1

    if (len(message) * 8) % 128 == 120:
        return f"{pad}{''.rjust(127, "0")}{length_pad}"
    elif (len(message) * 8) % 128 >= 120:
        return f"{pad}{"0"*(128 - ((len(message) * 8 + 1) % 128))}{length_pad.rjust(128, "0")}"
    else:
        return f"{pad}{''.rjust(more_pad, "0")}{length_pad}"

def main() -> None:
    # Tests for student side debugging only
    assert compute_pad("A" * 14) == "1000000000001110"
    assert compute_pad("A" * 15) == "1000000000000000000000000000000000000000000000000000000000000000" \
                                    "000000000000000000000000000000000000000000000000000000000000000000001111"
    assert compute_pad("A" * 16) == "1000000000000000000000000000000000000000000000000000000000000000" \
                                    "0000000000000000000000000000000000000000000000000000000000010000"
    assert compute_pad("A" * 300) == "10000000000000000000000000101100"


if __name__ == '__main__':
    main()
