
def decodificar(codigo):
    lista = codigo.split(",")
    decimales = []
    binarios2 = []
    for binario in lista:
        nuevo_binario = ""
        for i in range(1,len(binario)+1):
            nuevo_binario += binario[-i]
        binarios2.append(nuevo_binario)
    for elemento in binarios2:
        decimal = 0
        for j in range(len(elemento)):
            decimal = decimal + int(elemento[j]) * (2**j)
        decimales.append(decimal)
            
    palabra = []
    for n in decimales:
        palabra.append(chr(n))
    mensaje = "".join(palabra)
    return mensaje

if __name__ == "__main__":
    codigo = "01101000,01101111,01101100,01100001"
    mensaje=decodificar(codigo)
    print(mensaje)
         
         
if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         