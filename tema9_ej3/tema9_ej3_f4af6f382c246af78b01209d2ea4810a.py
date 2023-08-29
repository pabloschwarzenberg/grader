import math

def decodificar(mensaje):
    l = mensaje.split(",")
    l_reales = []
    l_letras = []
    i = 0
    while i < len(l):
        j = 0
        num = 0
        while j < len(l[i]):
            num = num + (int(l[i][j]) * (2**((len(l[i])-1)-j)))
            j+=1
        i+=1
        l_reales.append(num)
    i = 0
    while i < len(l_reales):
        l_letras.append(chr(l_reales[i]))
        i += 1
        
    mensaje = "".join(l_letras)
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         