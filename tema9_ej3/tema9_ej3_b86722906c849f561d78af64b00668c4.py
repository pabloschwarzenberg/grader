def decodificar(mensaje):
    caracteres = mensaje.split(",")
    i = 0
    palabra =[]
    while i < len(caracteres):
        numero = caracteres[i]
        decimal = int(numero,2)
        letra = chr(decimal)
        palabra.append(letra)
        i += 1

    mensaje = "".join(palabra)
    return mensaje
            
    
if __name__ == "__main__":
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
