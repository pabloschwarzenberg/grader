def decodificar(mensaje):
    mensaje=mensaje.split(',')
    mensajel=[]
    for i in mensaje:
        i=list(i)
        mensajel.append(i)
    for j in range(len(mensajel)):
        mensajel[j]=list(map(int,mensajel[j]))
    decmes=[]
    for k in range(len(mensajel)):
        deci=0
        for l in range(8):
            pot2=mensajel[k][l]*(2**(7-l))
            deci+=pot2
        decmes.append(deci)
    meslet=list(map(chr,decmes))
    mensaje=''.join(meslet)
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         