import random
def ocultar_letras(palabra,cantidad):
    patpot=[]
    for g in palabra:
        patpot.append(g)
    largo=len(palabra)
    lil=[]
    for g in range(largo):
        lil.append(g)
    for g in range(cantidad):
        o=random.choice(lil)
        lil.remove(o)
        patpot[o]="_"
    patpot="".join(patpot)
    return patpot
def revisar_letra(palabra_secreta,palabra,letra):
    bean1=[]
    bean2=[]
    
    for y in palabra_secreta:
        bean1.append(y)
    for y in palabra:
        bean2.append(y)
    for y in range(len(bean1)):
        if bean1[y] == letra:
            bean2[y] = letra
    lil2="".join(bean2)
    return lil2
