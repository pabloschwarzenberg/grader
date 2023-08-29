def genoma(string):
    codigo=string.lower()
    i=0
    while i<=len(codigo)-1:
        if (codigo[i]=="a") or (codigo[i]=="c") or (codigo[i]=="t") or (codigo[i]=="g"):
            genoma==True
        else:
            genoma==False
            break
        i+=1
    if genoma==True:
        c ="secuencia correcta"
        return c
    elif genoma==False:
        c= "secuencia incorrecta"
        return c
    