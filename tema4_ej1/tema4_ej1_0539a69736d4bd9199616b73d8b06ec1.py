import random
def ocultar_letras(palabra,cantidad):
    lista=list(palabra)
    lista1=""
    numeros=[]
    for i in range(len(palabra)):
        numeros.append(i)
    for r in range(cantidad):
        a=random.choice(numeros)
        numeros.remove(a)
        lista[a]="_"
    for i in lista:
        lista1+=str(i)
    return lista1
def revisar_letra(palabra_secreta,palabra,letra):
    lista1=list(palabra_secreta)
    lista2=list(palabra)
    lista3=""
    for i in range(len(lista1)):
        if lista1[i] == letra:
            lista2[i] = letra
    for i in lista2:
        lista3+=i
    return lista3
def letra_azar():
    lista=("tibio","grabar","carnaval","introducir")
    a=random.choice(lista)
    return a