#Ejercicio 9
def decodificar(mensaje):
    lista=mensaje.split(',')
    lista2=[]
    for i in range(len(lista)):
        lista2.append(chr(int(lista[i],2)))
    final=''.join(lista2)
    return final

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
    