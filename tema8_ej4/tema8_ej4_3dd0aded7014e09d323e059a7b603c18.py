def rot13(palabra):
    lista_1="abcdefghijklm"
    lista_2="nopqrstuvwxyz"
    palabra_nueva=""
    for i in palabra:
        if i in lista_1:
            posicion = lista_1.find(i)
            palabra_nueva = palabra_nueva + lista_2[posicion]  

        elif i in lista_2:
            posicion = lista_2.find(i)
            palabra_nueva = palabra_nueva + lista_1[posicion]

    return palabra_nueva

