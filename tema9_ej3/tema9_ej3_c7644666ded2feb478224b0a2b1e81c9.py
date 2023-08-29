def decodificar(mensaje):
    num_mensaje=mensaje.split(",")
    contador_a=0
    contador_b=1
    lista_decimal=[]
    lista_suma=[]
    lista_carac=[]

 

    for i in range(0,len(num_mensaje)):
        numero= num_mensaje[i]
        for j in range (0, len(numero)):
            decimales=int(numero[-contador_b])* 2 **contador_a
            lista_decimal.append(decimales)
            contador_a += 1
            contador_b += 1
            if contador_a==8:
                suma=sum(lista_decimal)
                lista_decimal=[]
                contador_a=0
                contador_b=1
                lista_suma.append(suma)
    for k in range(0,len(lista_suma)):
        caracter=chr(lista_suma[k])
        lista_carac.append(caracter)

 

    mensaje = "".join(lista_carac)
    return(mensaje)

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         