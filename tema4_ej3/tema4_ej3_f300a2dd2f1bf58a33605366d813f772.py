def jerigonzo(string):
    lista=[str(x) for x in string]
    y=0
    while y<len(lista):
        
        if "a"==lista[y]:
            lista[y]=("apa")
        elif "e"==lista[y]:
            lista[y]=("epe")
        elif "i"==lista[y]:
            lista[y]=("ipi")
        elif "o"==lista[y]:
            lista[y]=("opo")
        elif "u"==lista[y]:
            lista[y]=("upu")
        y+=1
    string=''.join(lista)
    return(string)

                
    

if __name__ == "__main__":
    pass
         