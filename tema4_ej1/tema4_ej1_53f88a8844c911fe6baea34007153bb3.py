from random import randint
palabras_secretas=["palabra","lepidoptero","elefante","estegosaurio"]
n=randint(0,len(palabras_secretas))
palabra=palabras_secretas[n]
cantidad=randint(0,len(palabra))

def ocultar_letras(palabra,cantidad):
    letras=list(palabra)
    i=1
    while i<=cantidad:
        numero=randint(0,len(palabra))
        if letras[numero]!="_":
            letras[numero]="_"
            i+=1
    palabra_oculta=""
    for x in letras:
        palabra_oculta+=x
    return palabra_oculta

def revisar_letra(palabra_secreta,palabra,letra):
    palabra=list(palabra)
    for x in range(len(palabra)):
        if letra==palabra_secreta[x]:
            palabra[x]=letra
    nueva_palabra=""
    for y in palabra:
        nueva_palabra+=y
    return nueva_palabra