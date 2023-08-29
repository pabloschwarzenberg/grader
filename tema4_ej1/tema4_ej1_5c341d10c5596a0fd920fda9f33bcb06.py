import random
palabras_secretas=["paralelepipedo","oftalmologo","caricatura"]
palabra=random.choice(palabras_secretas)
palabra="lepidoptero"
a=0
numero=len(palabra)
ocultas=random.randint(1,numero)
def ocultar_letras(a,b):
    letras=[]
    for letra in a:
        letras.append(letra)    
    while b>0:
        elegida=random.randint(0,len(a)-1)
        elegida2=letras[elegida]
        if elegida2=="_":
            pass
        else:
            elegida=int(elegida)
            p="_"
            letras[elegida]=p
            b=b-1
        a="".join(str(e) for e in letras)
    return a
def revisar_letra(palabra_normal,palabra_oculta,INPUT):
    letras_normal=[]
    letras_oculta=[]
    contador=0
    if len(INPUT)>1:
        if INPUT==palabra1:
            palabra2=INPUT
    elif len(INPUT)==1:
        for letra in palabra_normal:
            letras_normal.append(letra)
        for letra in palabra_oculta:
            letras_oculta.append(letra)
        for letra in letras_normal:
            if letra==INPUT:
                letras_oculta[contador]=INPUT
                contador=contador+1
            elif letra!=INPUT:
                contador=contador+1    
        palabra_final="".join(str(e) for e in letras_oculta)
    return palabra_final
if __name__ == "__main__":
    palabra_secreta=ocultar_letras(palabra,ocultas)
    while a<1:
        print("La palabra es: ",palabra_secreta)
        INPUT=input("Ingrese una letra o la palabra que usted crea que es: ")
        palabra_secreta=revisar_letra(INPUT,palabra,palabra_secreta)
        









        
        
    
