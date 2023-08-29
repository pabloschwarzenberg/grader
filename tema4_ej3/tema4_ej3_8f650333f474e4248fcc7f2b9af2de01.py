vocales = ["a", "e", "i", "o", "u"]


def jerigonzo(string):
    palabra = ""
    for a in string:
        palabra += a
        if a in vocales:
            palabra += "p"
            palabra += a

    return palabra


if __name__ == "__main__":
    a = input()
    print(jerigonzo(a))
    pass
         