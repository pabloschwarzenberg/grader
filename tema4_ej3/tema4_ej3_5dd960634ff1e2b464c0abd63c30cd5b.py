def jerigonzo(string):
    return string

if __name__ == "__main__":
    pass
def jerigonzo(original):
    traducida = ""
    for letra in original:
        traducida += letra
        if letra in "AEIOUaeiou":
            traducida += "p" + letra
    return traducida       