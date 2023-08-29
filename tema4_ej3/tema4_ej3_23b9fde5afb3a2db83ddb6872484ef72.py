def jerigonzo(string):
    i = ''
    v = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    for letra in string:
        if letra in v:
            i +=letra
            i += "p"
        i += letra
    return i

if __name__ == "__main__":
    palabra = input("Ingresa una palabra:")
    print(jeringonzo(palabra))
         