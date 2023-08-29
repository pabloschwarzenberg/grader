def decodificar(numeros_binarios):
    lista_NB=numeros_binarios.split(",")
    resultado=""
    for i in lista_NB:
        d= (int(str(i), 2))
        resultado=resultado+chr(d)
    return resultado
         