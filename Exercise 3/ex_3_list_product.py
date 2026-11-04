# Write a function called list_product, which takes a list of integers and returns their product. You have to use a for loop to do this!

def list_product(lst: list) -> int:
    if len(lst) == 0: return 0
    ret = 1
    for i in lst:
        ret *= i
    return ret


def main() -> None:
    assert list_product([1, 4, 7, 2]) == 56
    assert list_product([3, -8, -9, 12]) == 2592
    assert list_product([]) == 0

if __name__ == '__main__':
    main()
