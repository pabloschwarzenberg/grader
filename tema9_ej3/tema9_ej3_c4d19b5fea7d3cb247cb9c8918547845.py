def decodificar(mensaje):
    listo = []
    ramon=[]

    mensaje = mensaje.split(",")

    for i in range(len(mensaje)):

        k = int(mensaje[i],2)
        listo.append(k)

        if(i==len(mensaje)-1):

            for g in range(len(listo)):

                t=chr(listo[g])
                ramon.append(t)


    s = ''.join(ramon)
    
    return s

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         