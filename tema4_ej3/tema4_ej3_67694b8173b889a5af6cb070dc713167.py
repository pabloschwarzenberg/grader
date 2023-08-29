def jerigonzo(string):
    traduccion = ""
    for letra in string:
        if letra in "AEIOUaeiou":
            traduccion += letra
            traduccion += 'p'
        traduccion += letra
    return traduccion

if __name__ == "__main__":
    print(jerigonzo('solia'))