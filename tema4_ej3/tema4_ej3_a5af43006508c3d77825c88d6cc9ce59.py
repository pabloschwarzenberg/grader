def jerigonzo(string):
    t = ""
    for i in string:
        if i in "AEIOUaeiou":
            t+=i
            t+="p"
        t+=i    
    return t

if __name__ == "__main__":
    palabra = input("Ingrese palabra: ")
    xd = jerigonzo(palabra)
    print(xd)
    pass