def jerigonzo(string):
    s=""
    for i in range(len(string)):
        s=s+string[i]
        if string[i]=="a" or string[i]=="e" or string[i]=="i" or string[i]=="o" or string[i]=="u":
            s=s+"p"+string[i]
    string=s
    return string

if __name__ == "__main__":
    print(jerigonzo(input("ingrese texto")))
    pass
         