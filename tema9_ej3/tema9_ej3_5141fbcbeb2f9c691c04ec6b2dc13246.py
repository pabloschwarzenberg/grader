def decodificar(mensaje):
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
    
    numero = int(input("ingrese numero entero: "))

binario = bin(numero)[2:]

print("resultado=", binario)
         