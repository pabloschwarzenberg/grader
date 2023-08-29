def jerigonzo(palabra):
    b=""
    for h in palabra:
        if h=="a" or h=="e" or h=="i" or h=="o" or h=="u":
            b=b+h+"p"+h
        else:
            b=b+h
    return b

if __name__ == "__main__":
    print(jerigonzo(input("ingrese palabra: ")))
         