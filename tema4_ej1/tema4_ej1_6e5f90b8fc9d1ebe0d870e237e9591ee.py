import random
def ocultar_letras(palabra,cantidad):
    cantidad=cantidad
    palabra1=list(palabra)
    posiciones=[]
    for i in range(0,cantidad):
        pos = random.randint(0, len(palabra1) - 1)
        pos1=str(pos)
        if ( pos1 in posiciones) != True:
            posiciones.append(pos1)
            cantidad+= (-1)
    while len(posiciones)!=0:
        palabra1[int(posiciones[0])]= "_"
        posiciones.pop(0)
    palabra2="".join(palabra1)

    return palabra2
def revisar_letra(palabra_secreta,palabra,letra):
    palabra1 = list(palabra)
    for i in range(0,len(palabra)):
        if palabra_secreta[i]== letra:
              palabra1[i]= letra

    palabra_final="".join(palabra1)
    return palabra_final





if __name__ == "__main__":
    pass
         