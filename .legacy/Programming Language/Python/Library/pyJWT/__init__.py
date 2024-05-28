from time import sleep, time
from jwt import encode, decode
from datetime import datetime, timedelta
from datetime import timezone


def kst_now():
    return datetime.utcnow() + timedelta(hours=9)


# _validate_exp

# (datetime.utcnow() + timedelta(seconds=20)).timestamp() => Error

# datetime
# kst_now => 1714641906 = 2024, 5, 2, 18, 25, 6
# utc_now => 1714609489 = 2024, 5, 2, 9, 24, 49

# timestamp
# kst_now => 1714609570 = 2024, 5, 2, 9, 26, 10
# utc_now => 1714577185 = 2024, 5, 2, 0, 26, 25


if __name__ == '__main__':
    start_at = time()
    token = encode({'exp': (datetime.utcnow() + timedelta(hours=9)).timestamp()}, key='enlwuTdmauswhgrpTek',
                   algorithm='HS256')
    print(token)

    now = time()

    print(decode(token, key='enlwuTdmauswhgrpTek', algorithms='HS256'))

    sleep(21)

    try:
        print(decode(token, key='enlwuTdmauswhgrpTek', algorithms='HS256'))
    except Exception as e:
        print(e, now)
