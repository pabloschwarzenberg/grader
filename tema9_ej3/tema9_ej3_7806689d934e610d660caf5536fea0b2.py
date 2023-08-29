def decodificar(mensaje):
    mensaje=mensaje.split(",")
    numeros=[]
    letras=[]
    for i in range(len(mensaje)):
        a=mensaje[i]
        n=int()
        h=1
        for k in a[2:8]:
            n=h*2+int(k)
            h=n
        numeros.append(h)    
    for t in numeros:
        letras.append(chr(t))
    return(letras[0]+letras[1]+letras[2]+letras[3])

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)


         