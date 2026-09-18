#!/usr/bin/env python3
"""Self-contained: prints a distant, blurry ghost as 24-bit ANSI art (30 cols x 14 rows)."""
import base64, sys, zlib

_DATA = (
    "eNqVWM253CAMvKeFXF4JtrHX5kspqcE9pIoUmEqyIIQ1QhL7lrl4YY0YjX7Yr6/o8/P3cv+A5/36tdG430+pPK1l3G3qKuP+"
    "9/dPm0xl8GQuQ0y+yuDJdSGI+aOMPr8T2nzm788ybjaNjKmGBwexLCdLnc3J0meSTsJ7Noj59STwki0R5JKDwEv2nSCWbAuh"
    "v2UnyLe8KUlvdFsugssispzx9Jo3pE1TXN++l9HPUB+erUkN4Chh+kropqV2FEFAJnQrG6SGTkL3VIMkYCX0t2SC3GgldFvY"
    "Och01R8veRE8pmUkPFKx5KlZTk+MQcA9GwHptOszSTwLK85AdZZ2k5IU+0nsfxC63xtk4LOr2C8LwQuiYyFIQzKhs8DhIJaw"
    "nJ0MA+lHEOXQr4NBiNrOfaH6QQ7aS5D7pqExumB7EYL0qb1UFK74SwchCLA9Eb6RyrQXtJcM0QFXgg7bUZZ3NYeQewwCMYWP"
    "uQfCyGAXNtdlD7yriwe8eXD9RNFDdLupXstRiyq02TiwwWF3pE9zeFhIcqIAC68PTtdm67y8NUhXrRVboPL+KyZvIURBOdYI"
    "VQBOMBQEOQ2Rkf9QCcP7dAPC6UIs4QLmp1eMEcP/s7AaT4FhlSARZJQmlEnI0snKqCkRnIaxLnkRZEasZV87InuKnTV+WTp5"
    "kOo8rcP7XZH4LaLR//WveAlLw1dfN9xX3xD6YJtHDwS8SFDdz7IX+qSM9pY4qE66nzHOr0LBsDzMux84NsjrnlqHGD4IkeFj"
    "U3pFigx7xStKMFhejWqh9TFWWGieRItricHsvuJCCpEgM/b+PTOhLuqiCvGqC318/dGuM64/LOagAeYe+fMOIrQKKA1vvVZC"
    "mMQAtExWuR+TvL75gDOGChD1g7PCNGuPwjSk7gH4T0Jos952VsitC5u+mY6HC00Qz/NbvP5xGADe9ShK915WmMdiaCe4T//X"
    "A8Lpe0L9CxmEncOo0aoML5B2vOgfm44MjuXQb4VcXai/NvbXBV5os/7h4S3Rff5/Rbd3bg=="
)

def ghost_distant() -> str:
    return zlib.decompress(base64.b64decode(_DATA)).decode("utf-8")

if __name__ == "__main__":
    sys.stdout.write(ghost_distant())
