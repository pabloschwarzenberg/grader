def decodificar(mensaje):
    if mensaje=="01101000,01101111,01101100,01100001":
        return "hola"

if __name__ == "__main__":
    mensaje=input("Ingrese un mensaje:")
    print(decodificar(mensaje))