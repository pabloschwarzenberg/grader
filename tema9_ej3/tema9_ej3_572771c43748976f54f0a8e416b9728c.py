def decodificar(mensaje):
    string = ""
    a = mensaje.split(',')
    for x in range(len(a)):
        suma = 0
        for letra in range(len(a[x])):
            let = a[x][-letra-1]
            suma += int(let)*(2**letra)
        string += chr(suma)
    return string
    
if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         