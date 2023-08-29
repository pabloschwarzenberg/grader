def jerigonzo(string):
    jerigonzo=""
    i=0
    for j in string:
        if string[i]=="a" or string[i]=="e" or string[i]=="i" or string[i]=="o" or string[i]=="u":
            jerigonzo=jerigonzo+string[i]+"p"+string[i]
            i=i+1
        else:
            jerigonzo=jerigonzo+string[i]
            i=i+1
        
    return jerigonzo

if __name__ == "__main__":
    string=input("ingrese la palabra:")
    print(jerigonzo(string))
