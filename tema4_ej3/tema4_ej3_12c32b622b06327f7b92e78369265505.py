def jerigonzo(string):
    jerigo = ""
    for letra in string:
        if letra in "AEIOUaeiou":
            jerigo += letra
            jerigo += "p"
        jerigo += letra
    return jerigo
if __name__ == "__main__":
    pass
         