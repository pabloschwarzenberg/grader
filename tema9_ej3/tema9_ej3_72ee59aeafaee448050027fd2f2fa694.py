def decodificar(numeros_binarios):
    lista_NB=numeros_binarios.split(",")
    resultado=""
    for i in lista_NB:
        d= (int(str(i), 2))
        resultado=resultado+chr(d)
    return resultado

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         