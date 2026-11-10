import string


def frequency_analysis(file_directory: str) -> dict[str, int]:
    freq = {}
    for c in string.ascii_lowercase:
        freq[c] = 0
    with open(file_directory) as f:
        for line in f:
            for c in line:
                c = c.lower()
                if c in freq:
                    freq[c] = freq[c] + 1
        f.close()
    print(freq)
    return freq