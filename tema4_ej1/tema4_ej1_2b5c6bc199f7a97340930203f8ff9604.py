import random
def ocultar_letras(palabra,cantidad):
    grupo=[]
    for k in palabra:
        grupo.append(k)
    longitud=len(palabra)
    grupo1=[]
    for k in range(longitud):
        grupo1.append(k)
    for k in range(cantidad):
        aleatorio=random.choice(grupo1)
        grupo1.remove(aleatorio)
        grupo[aleatorio]= "_"
    grupo= "".join(grupo)
    return grupo
def revisar_letra(palabra_secreta,palabra,letra):
    grupo1=[]
    grupo2=[]
    for k in palabra_secreta:
        grupo1.append(k)
    for k in palabra:
        grupo2.append(k)
    for k in range(len(grupo1)):
        if grupo1[k] == letra:
            grupo2[k] = letra
    conjunto2= "".join(grupo2)
    return conjunto2