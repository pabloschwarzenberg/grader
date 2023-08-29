import random
def ocultar_letras(palabra,cantidad):
    li=[]
    for i in palabra:
        li.append(i)
    la=len(palabra)
    l1=[]
    for i in range(la):
        l1.append(i)
    for i in range(cantidad):
        a=random.choice(l1)
        l1.remove(a)
        li[a]="_"
    li="".join(li)
    return li
def revisar_letra(palabra_secreta,palabra,letra):
    li_num1=[]
    li_num2=[]
    for i in palabra_secreta:
        li_num1.append(i)
    for i in palabra:
        li_num2.append(i)
    for i in range(len(li_num1)):
        if li_num1[i] == letra:
            li_num2[i] = letra
    li2="".join(li_num2)
    return li2