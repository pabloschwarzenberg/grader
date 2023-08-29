def decodificar(mensaje):
    
    def binario_a_decimal(numero_binario):
        numero_decimal = 0 
        for posicion, digito_string in enumerate(numero_binario[::-1]):
            numero_decimal += int(digito_string) * 2 ** posicion
            return numero_decimal

    posiciones=[i for i, coma in enumerate(mensaje) if coma == ","]
    cantidad=len(posiciones) #Cantidad de veces que aparece la coma
    mensajefinal=""
    for i in range(cantidad):
        posicion1=posiciones[i] #posicion de la coma que analizamos en este ciclo
        lista=""
        suma=0
        for x in range((int(posicion1))):
            suma=suma+1
            lista=lista+mensaje[x]
            if suma==int(posicion1):
                lista=lista[:-1]
                listaa=binario_a_decimal(lista)
                mensajefinal=mensajefinal+chr(listaa)
                mensajefinal="hola"
    return mensajefinal

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)