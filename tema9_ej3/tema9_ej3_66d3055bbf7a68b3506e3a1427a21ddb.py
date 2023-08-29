def decodificar(mensaje):
    a = mensaje.split(',')
    palabra = list()
    for x in range(0,len(a)):
        d = int(a[x], 2) 
        palabra.append(chr(d))
    palabra_final = "".join(palabra)

    print(palabra_final)
    return palabra_final

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         