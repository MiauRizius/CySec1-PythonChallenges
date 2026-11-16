def unique_IPs(ip_list: list[str]) -> list[str]:
    alr_exist = {}
    unique_list = []
    for idx, ip in enumerate(ip_list):
        if ip in alr_exist and alr_exist[ip] != idx:
            pass
        else:
            alr_exist[ip] = idx
            unique_list.append(ip)
    return unique_list



def main() -> None:
    # Tests for student side debugging only
    assert unique_IPs(["47.78.23.151", "211.216.183.149", "47.78.23.151", "116.118.242.134"]) == ["47.78.23.151", "211.216.183.149", "116.118.242.134"]
    assert unique_IPs(['29.66.248.231', '29.66.248.231', '29.66.248.231']) == ['29.66.248.231']


if __name__ == '__main__':
    main()
