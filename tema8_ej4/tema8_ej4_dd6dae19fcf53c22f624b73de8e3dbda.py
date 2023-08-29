def rot13(palabra):
    lisPalabraCodigo=[]
    for i in range(0,len(palabra)):
        letraASCII=ord(palabra[i])
        lisPalabraCodigo.append(letraASCII)

    lisNueva=[]
    for i in range(0,len(lisPalabraCodigo)):
        if lisPalabraCodigo[i]>=65 and lisPalabraCodigo[i]<=77 or lisPalabraCodigo[i]>=97 and lisPalabraCodigo[i]<=109:
            nueva=lisPalabraCodigo[i]=lisPalabraCodigo[i]+13
            caracter=chr(nueva)
            lisNueva.append(caracter)

        elif lisPalabraCodigo[i]>=78 and lisPalabraCodigo[i]<=90 or lisPalabraCodigo[i]>=110 and lisPalabraCodigo[i]<=122:
            nueva=lisPalabraCodigo[i]=lisPalabraCodigo[i]-13
            caracter=chr(nueva)
            lisNueva.append(caracter)

    strFinal="".join(lisNueva)
    return(strFinal)