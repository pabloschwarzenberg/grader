import random
def ocultar_letras(palabra,cantidad):
    pos = []
    x = 0
    while x != cantidad:
        p = random.randint(0,len(palabra)-1)
        if p not in pos:
            pos.append(p)
            x+=1 
    Palabra = []
    for x in palabra:
        Palabra.append(x)
    for x in pos:
        Palabra[x] = '_'
    palabra = ''
    for i in Palabra:
        palabra+=i
    return palabra
def revisar_letra(palabra_secreta,palabra,letra):
    pos = []
    for i in range(0,len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            pos.append(i)
    Palabra = []
    for x in palabra:
        Palabra.append(x)
    palabra = ''
    for x in pos:
        if Palabra[x] == '_':
            Palabra[x] = letra
    for x in Palabra:
        palabra+=x
    return palabra
            
      