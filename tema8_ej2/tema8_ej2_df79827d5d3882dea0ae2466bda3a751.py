def buscarTodas(a,b):
    buscador = [i for i, x in enumerate(a) if x == b]
    lista_1 = list(buscador)
    lista_2 = []
    for i in lista_1:
        lista_2.append(str(i))
    termino =" ".join(lista_2)
    return termino

if __name__ == "__main__":
    buscarTodas("tres tristes tigres","t")