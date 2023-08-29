import random
import string
from random import randint
personajes_marvel=["Loki","IronMan","CapitanAmerica","Wolverine","Thor","lepidoptero"]
personaje=random.choice(personajes_marvel)
cantidad_letras=len(personaje)
cantidad_letras_ocultar=randint(0,cantidad_letras)
palabra_secreta=personaje

def ocultar_letras(personaje,cantidad_letras_ocultar):
    personaje=list(personaje)
    for j in range(cantidad_letras_ocultar):
        i=randint(0,cantidad_letras+1)
        if personaje[i]!="_":
            personaje[i]="_"
        else:
            personaje=personaje
    personaje="".join(personaje)
    return personaje

def revisar_letra(palabra_secreta,personaje,letra):
    letra=letra.lower()
    palabra_secreta=palabra_secreta.lower()
    personaje=personaje.lower()
    palabra_secreta=list(palabra_secreta)
    personaje=list(personaje)
    contador=0
    j=0
    while contador<=7:
        while j<=cantidad_letras_ocultar:
            for i in range(cantidad_letras):
                if personaje[i]=="_" and palabra_secreta[i]==letra:
                    personaje[i]=letra
                    j+=1
        palabra_secreta="".join(palabra_secreta)
        personaje="".join(personaje)
        contador+=1
    return personaje

if __name__ == "__main__":
    pass
         
