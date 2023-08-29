# -*- coding: utf-8 -*-

def buscarTodas(a,b):
    listaCoincidencias = []
    largo = len(a)
    i = 0
    while i < largo:
        pos = i
        if a[i] == b:
            listaCoincidencias.append(pos)
        i = i + 1
    return (listaCoincidencias)
    pass

if __name__ == "__main__":
    a ="tres tristes tigres"
    b = "t"
    coincidencias = buscarTodas(a,b)
    i = 0 
    palabra = ""
    while i < len(coincidencias):
        if i == (len(coincidencias)-1):
            palabra = palabra + str(coincidencias[i])
        else:
            palabra = palabra + str(coincidencias[i]) + " "
        i = i + 1
    print (palabra)
    pass