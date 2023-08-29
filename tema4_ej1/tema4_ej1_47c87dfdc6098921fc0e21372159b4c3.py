import random
def ocultar_letras(palabra,cantidad):
    c=len(palabra)
    lista=[]
    intentos=0
    for d in range (c):
        lista.append(palabra[d])
    while intentos<4:
        i=random.randint(0,c-1)
        if lista[i]!="_":
            lista.pop(i)
            lista.insert(i,"_")
            intentos=intentos+1
    palabraoculta=""
    for o in range(c):
        palabraoculta=palabraoculta+lista[o]
    palabra=palabraoculta
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    global intentos
    intentos=0
    lista=[]
    c=len(palabra)
    palabrarevelada=""
    for d in range (c):
        f=palabra_secreta[d]
        p=palabra[d]
        if f==letra:
            lista.append(f)
        else:
            lista.append(p)
    intentos=intentos+1
    for h in range(c):
        palabrarevelada=palabrarevelada+lista[h]
    palabra=palabrarevelada
    return palabra

if __name__ == "__main__":
    pass
intentos=0