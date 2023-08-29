def decodificar(numeros_binarios):
    lista_numeros_binarios=numeros_binarios.split(",")
    resultado=""
    for i in lista_numeros_binarios:
        decodificador= (int(str(i), 2))
        resultado += chr(decodificador)
    return resultado

if __name__ == "__main__":

    numeros_binarios=decodificar("01101000,01101111,01101100,01100001")
    print(numeros_binarios)
