import random
def palabra_secreta():
    global palabras_secretas
    a=random.randint(0,6)
    return palabras_secretas[a]
def ocultar_letras(palabra, cantidad):
    a=0
    b=0
    while cantidad>=0:
        a=b
        b=random.randint(0,len(palabra)-1)
        if not(a==b):
            palabra=palabra.replace(palabra[b],'_',1)
            cantidad-=1
    return palabra
def revisar_letra(palabra_secreta,palabra,letra):
    letras_ocultas=[]
    pos=0
    for i in palabra:
        letras_ocultas.append(i)
    for i in palabra_secreta:
        if i==letra:
            letras_ocultas[pos]=letra
        pos+=1
    palabra=''
    for i in letras_ocultas:
        palabra=palabra+i
    return palabra
if __name__ == "__main__":
    pass
         
         
         