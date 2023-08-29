def jerigonzo(s):
    vocales="aeiou"
    for i in vocales:
        s=s.replace(i,i+"p"+i)
    return s
if __name__ == "__main__":
    s=input("Ingresa un string: ")
    print(jerigonzo(s))