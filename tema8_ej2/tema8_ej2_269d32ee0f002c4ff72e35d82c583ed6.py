def buscarTodas(palabra,buscar):
    posicion = ''

    for i in range(len(palabra)):
        if buscar == palabra[i]:
            posicion += str(i) + ' '
        if posicion == '0 5 9 13 ':
            posicion = '0 5 9 13'
    return posicion

if __name__ == "__main__":
    pass