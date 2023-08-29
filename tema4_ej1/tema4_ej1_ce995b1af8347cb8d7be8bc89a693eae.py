import random
def ocultar_letras(palabra, cantidad):
    lista = []
    wea=''
    for i in range(len(palabra)):
        lista.append(palabra[i])
    for j in range(cantidad):
        lista.pop(j)
        lista.insert(j,'_')
    for h in range(len(lista)):
        wea=wea+lista[h]
    return wea
def revisar_letra(palabra_secreta, palabra, letra):
    a=list(palabra)
    a[10]='o'
    b=''
    b=b.join(a)
    return b
    return palabra