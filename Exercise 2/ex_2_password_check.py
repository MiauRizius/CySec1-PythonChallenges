def password_check(username: str, password: str) -> str:
    redflags = 0

    if(len(password) < 12):
        redflags += 1
    if(password.find(username) != -1 or "password" in password or "qwert" in password or "12345" in password):
        redflags += 1
    if password.isalnum():
        redflags += 1

    if redflags == 0:
        return "good"
    elif redflags == 1:
        return "Ok"
    elif redflags == 2:
        return "weak"
    else:
        return "bad"

def main() -> None:
    # Tests only for student side debugging
    assert password_check("Hans", "asdhf2324#fq1sa") == "good"
    assert password_check("Dieter", "securepassword!") == "Ok"
    assert password_check("Kevin", "Kevin2002!") == "weak"
    assert password_check("Bob", "qwertz") == "bad"


if __name__ == '__main__':
    main()
