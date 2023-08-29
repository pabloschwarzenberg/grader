def decodificar(mensaje):
    l_binarios = mensaje.split(",")
    i=0
    lista=[]
    while len(l_binarios)>i:
        binario= l_binarios[i]
        valor = int(binario[7])*(2**0) + int(binario[6])*(2**1) + int(binario[5])*(2**2) + int(binario[4])*(2**3) + int(binario[3])*(2**4) + int(binario[2])*(2**5) + int(binario[1])*(2**6) + int(binario[0])*(2**7)
        letra = chr(valor)
        lista.append(letra)
        i = i + 1
    lista2 ="".join(lista)
    return lista2
    
if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
    

         