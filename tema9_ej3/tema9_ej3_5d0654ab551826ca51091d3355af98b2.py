def decodificar(mensaje):
    mLista=mensaje.split(",")
    palabra=""
    for i in range(len(mLista)):
        numero=int(mLista[i],2)
        letra=chr(numero)
        palabra=palabra+"".join(letra)
    return palabra

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         