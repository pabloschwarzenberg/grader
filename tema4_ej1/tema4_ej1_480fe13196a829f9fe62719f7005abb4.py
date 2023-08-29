import random
lista=["pizza","hamburguesas", "papas con ketchup","completo italiano"]
palabra=random.choice(lista)
def ocultar_letras(palabra,cantidad):
    while cantidad>0:
        palabra1=list(palabra)
        c=random.choice(palabra)
        palabra.replace("c","_",1)
        cantidad=cantidad-1
        palabra1=[x for x in palabra if x != c]
        
def revisar_letra(palabra_secreta,palabra,letra):
    palabra=list(palabra)
    c=palabra.index("_")
    while palabra_secreta[c:c+1]==letra:
        palabra.replace("palabra[c:c1]","letra")
        palabra=[x for x in palabra if x != c]     