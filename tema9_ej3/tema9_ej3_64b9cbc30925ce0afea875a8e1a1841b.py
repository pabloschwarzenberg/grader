def decodificar(mensaje):
    string_binario = mensaje
    lista_binario = string_binario.split(",")
    palabra = ""
    for i in lista_binario:
        numero= i
        largo=len(numero)
        g=0
        entero=0
        while g<largo:
            potencia=2**(largo-g-1)
            digito=int(numero[g])
            entero=entero+digito*potencia
            g+=1
        palabra = palabra+chr(entero)
    return palabra

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         