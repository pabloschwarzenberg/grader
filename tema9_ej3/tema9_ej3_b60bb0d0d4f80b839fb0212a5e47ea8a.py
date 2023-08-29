def decodificar(mensaje):
    lista=[]
    s=0
    r=-1
    e=7
    for i in mensaje:
        lista.append(i)
    mensaje=""
    while r<len(lista):
        r=r+1
        SS=0
        e=7
        while lista[r]!=",":
            lista[r]=int(lista[r])
            s=lista[r]*2**e
            e=e-1
            SS=SS+s
            SS=int(SS)
            r=r+1
            if r==len(lista):
                break
        letra=chr(SS)
        mensaje=mensaje+letra
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         