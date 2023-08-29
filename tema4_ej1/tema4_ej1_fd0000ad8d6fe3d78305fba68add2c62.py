import random
def ocultar_letras(palabra,cantidad):
    lista=[]
    for i in palabra:
        lista.append(i)
    largo=len(palabra)
    l1=[]
    for i in range(largo):
        l1.append(i)
    for i in range(cantidad):
        a=random.choice(l1)
        l1.remove(a)
        lista[a]="_"
    lista="".join(lista)
    return lista
def revisar_letra(palabra_secreta,palabra,letra):
    lista_num1=[]
    lista_num2=[]
    for i in palabra_secreta:
        lista_num1.append(i)
    for i in palabra:
        lista_num2.append(i)
    for i in range(len(lista_num1)):
        if lista_num1[i] == letra:
            lista_num2[i] = letra
    lista2="".join(lista_num2)
    return lista2
