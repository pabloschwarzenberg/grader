import random
lista=["calculadora","camisa","abeja","zapallo","gallina","engranaje"]
palabra=random.choice(lista)
def ocultar_letras(palabra,cantidad):
    palabra_l=list(palabra)
    for n in range(cantidad):
        b=random.randint(0,len(palabra_l)-1)
        if palabra_l[b]!="_":
            palabra_l[b]="_"
            ocultar_letras(palabra,(cantidad)-1)
        else:
            ocultar_letras(palabra,cantidad-n)    
    return palabra_l
def revisar_letra(palabra_secreta,palabra,letra):
    palabra_secreta_l=list(palabra_secreta)
    palabra_l=list(palabra)
    for m in range(len(palabra_secreta_l)):
        if palabra_secreta_l[m]==letra:
            palabra_l[m]=letra
    palabra_l="".join(palabra_l)
    return palabra_l
         