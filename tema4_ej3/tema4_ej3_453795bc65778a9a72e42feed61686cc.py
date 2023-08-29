def jerigonzo(string):
    a=""
    string 
    for letra in string:
        if letra in "AEIOUaeiou":
            a += letra
            a += "p"
        a += letra
    return a

if __name__ == "__main__":
    string=input("ingresa una palabra: ")
    print (jerigonzo(string))