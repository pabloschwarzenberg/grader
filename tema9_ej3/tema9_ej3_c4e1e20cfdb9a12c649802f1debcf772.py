def decodificar(mensaje):
    separar=mensaje.split(",")
    listavalores=[]
    val=[]
    for i in separar:
        sumando=0
        l=len(i)
        for a in i:
            if a =="1":
                sumando=sumando+2**(l-1)
            l-=1
        listavalores.append(sumando)
    for i in listavalores:
         val.append(chr(i))
    fin="".join(val)
    return fin
if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         