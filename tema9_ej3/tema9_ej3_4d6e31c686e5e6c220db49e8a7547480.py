def decodificar(mensaje):
    binarios = list(map(str, mensaje.split(",")))
    binario1 = list(binarios[0])
    binario2 = list(binarios[1])
    binario3 = list(binarios[2])
    binario4 = list(binarios[3])

    binario1 = list(map(int, binario1))
    binario2 = list(map(int, binario2))
    binario3 = list(map(int, binario3))
    binario4 = list(map(int, binario4))


    n1 = binario1[0]*(2**7) + binario1[1]*(2**6) + binario1[2]*(2**5) + binario1[3]*(2**4) + binario1[4]*(2**3) + binario1[5]*(2**2) + binario1[6]*(2**1) + binario1[7]*(2**0)
    n2 = binario2[0]*(2**7) + binario2[1]*(2**6) + binario2[2]*(2**5) + binario2[3]*(2**4) + binario2[4]*(2**3) + binario2[5]*(2**2) + binario2[6]*(2**1) + binario2[7]*(2**0)
    n3 = binario3[0]*(2**7) + binario3[1]*(2**6) + binario3[2]*(2**5) + binario3[3]*(2**4) + binario3[4]*(2**3) + binario3[5]*(2**2) + binario3[6]*(2**1) + binario3[7]*(2**0)
    n4 = binario4[0]*(2**7) + binario4[1]*(2**6) + binario4[2]*(2**5) + binario4[3]*(2**4) + binario4[4]*(2**3) + binario4[5]*(2**2) + binario4[6]*(2**1) + binario4[7]*(2**0)

    lista = [chr(n1), chr(n2), chr(n3), chr(n4)]
    palabra = "".join(lista)
        
    return palabra


if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)