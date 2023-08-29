def jerigonzo(string):
    a=""
    string 
    for letra in string:
        if letra in "AEIOUaeiou":
            a += letra
            a += "p"
        a += letra
    return a


    string=input("ingresa alguna palabra: ")
    print (jerigonzo(string))
         