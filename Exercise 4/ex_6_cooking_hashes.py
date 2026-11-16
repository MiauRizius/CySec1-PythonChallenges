from hashlib import sha256


def cook_password(pw: str, salt: str = None, pepper: str = None) -> str:
    if pepper is None and salt is None:
        return sha256(pw.encode()).hexdigest()
    elif pepper is None and (salt is not None and salt != ""):
        return sha256(f"{pw}{salt}".encode()).hexdigest()
    else:
        return sha256(f"{pepper}{sha256(f"{pw}{salt}".encode()).hexdigest()}".encode()).hexdigest()


print(cook_password("WX5Qj5iDehv3uR5xgRTn1"))
print(cook_password("fhyVGxb"))
print(cook_password("mOCkidPw58t7padN8U72UmBLE7mH2rp6", "dex", "Abk"))