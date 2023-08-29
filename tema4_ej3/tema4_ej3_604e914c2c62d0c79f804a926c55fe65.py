def jerigonzo(string):
    lista=string.split( )
    i=0
    r=""
    for palabr in lista:
        palabra=str(lista[i])
        palabra=list(palabra)
        i=i+1
        j=0
        for letra in palabra:
            if palabra[j]=="a" or palabra[j]=="e" or palabra[j]=="i" or palabra[j]=="o" or letra=="u":
                palabra[j]=palabra[j]+"p"+palabra[j]
                j=j+1
            else:
                j=j+1
        palabrajeri="".join(palabra)
        if i!=1:
            palabrajeri=" "+palabrajeri
        r=r+palabrajeri
    string=r
    return string