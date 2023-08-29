import math
def decodificar(mensaje):
    numeros = mensaje.split(',')
    mensaje = ""
    for n in numeros:
        decimal = 0
        j = 0
        for i in range(len(n)-1,-1,-1):
            decimal += int(int(n[i])*math.pow(2,j))
            j += 1
        mensaje += chr(decimal)
    return mensaje

if __name__ == "__main__":
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         