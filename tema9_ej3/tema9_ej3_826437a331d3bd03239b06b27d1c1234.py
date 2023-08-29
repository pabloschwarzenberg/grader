def decodificar(mensaje):
    mensaje_separado = []
    guardado = [0]
    x = 1
    for i in range(len(mensaje)):
        if mensaje[i] == ",":
            guardado.append(i)
    guardado.append(len(mensaje))
    mensaje_separado.append(mensaje[guardado[0]:guardado[1]])
    for i in guardado:
        if x > 2:
            j = guardado.index(i)
            mensaje_separado.append(mensaje[guardado[j - 1] + 1:i])
        x += 1
    mensaje = ""
    for i in mensaje_separado:
        i = list(i)
        suma = 0
        for j in range(len(i)):
            numero = int(i[j])
            print(numero)
            print(numero * (2**(len(i)-j)))
            print(2**(len(i)-j))
            suma += numero * (2**(len(i)-j))
            print(suma)
        suma = int(suma/2)
        print(suma)
        mensaje += chr(suma)
        print(mensaje)
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         