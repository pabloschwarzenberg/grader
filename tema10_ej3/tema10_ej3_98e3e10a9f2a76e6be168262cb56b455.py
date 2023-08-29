def leer_sopa_de_letras(archivo):
    with open(archivo, "r") as archivo_sopa:
        lista_sopa = archivo_sopa.readlines()
        for indice in range(len(lista_sopa)):
            lista_sopa[indice] = lista_sopa[indice]. replace("\n", "").replace(" ", "").lower()
    return lista_sopa

def encontrar_la_palabra(palabra, sopa):
    for fila,linea in enumerate(sopa):
        if palabra in linea:
            print(f"Si existe en la fila {fila}")
            for num_letra in range(len(linea)):
                if palabra == linea[num_letra:num_letra+len(palabra)]:
                    print(f"columna {num_letra}")
                    return fila,num_letra