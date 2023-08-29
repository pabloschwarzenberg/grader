def jerigonzo(string):
    nuevostring=""
    for i in string:
        if (i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
            nuevostring=nuevostring+i+"p"+i
        elif(i!="a" or i!="e" or i!="i" or i!="o" or i!="u"):
            nuevostring=nuevostring+i
        
    return nuevostring

if __name__ == "__main__":
    pass
    string=input("Ingrese un string ")
    print(jerigonzo(string))