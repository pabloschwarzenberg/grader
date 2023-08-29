def jerigonzo(string):

    x = ""
    for letra in string:
        if letra in "AEIOUaeiou":
            x +=letra
            x += "p"
        x+=letra
    return x


if __name__ == "__main__":
    pass