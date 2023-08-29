import random
def ocultar_letras(palabra,cantidad):
    list=[]
    for i in palabra:
        list.append(i)
    largo=len(palabra)
    l1=[]
    for i in range(largo):
        l1.append(i)
    for i in range(cantidad):
        a=random.choice(l1)
        l1.remove(a)
        list[a]="_"
    list="".join(list)
    return list
def revisar_letra(palabra_secreta,palabra,letra):
    list_number1=[]
    list_number2=[]
    for i in palabra_secreta:
        list_number1.append(i)
    for i in palabra:
        list_number2.append(i)
    for i in range(len(list_number1)):
        if list_number1[i] == letra:
            list_number2[i] = letra
    list2="".join(list_number2)
    return list2