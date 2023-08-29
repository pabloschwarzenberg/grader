import random
def ocultar_letras(palabra,cantidad):
    palabra=list(palabra)
    for i in range(cantidad):
        while palabra.count('_')<cantidad:
            palabra[random.randint(1,len(palabra)-1)]='_'
    texto=''
    for i in range(len(palabra)):
        texto+=palabra[i]
    return texto 

def revisar_letra(palabra_secreta,palabra,letra):
    veces=palabra.count('_')
    x=0
    for i in range(veces-1):
        x=palabra.index('_',x)
        if palabra_secreta[x]==letra:
            palabra=palabra[:x]+letra+palabra[x+1:]
        x+=1
    if palabra[-1]=='_':
            palabra=palabra[:-1]+letra
    return palabra
'''
if __name__ == "__main__":
    fobias=['Astrafobia','Acrofobia','Aerofobia','Amaxofobia','Aracnofobia','Cinofobia','Claustrofobia','tripofobia']
    palabra_secreta=fobias[random.randint(0,len(fobias)-1)]
    cantidad=random.randint(1,len(palabra_secreta)-1)
    c=0
    adivinando=''
    palabra=ocultar_letras(palabra_secreta,cantidad)
    while c<7 and adivinando!=palabra_secreta and palabra!=palabra_secreta:
        print(palabra)
        adivinando=input()
        palabra=revisar_letra(palabra_secreta,palabra,adivinando)
        c+=1
    if adivinando==palabra_secreta or palabra==palabra_secreta:
        print('has ganado')
    else:
        print('has perdido')
'''
