hombre_imaginario = """
El hombre imaginario
vive en una mansión imaginaria
rodeada de árboles imaginarios
a la orilla de un río imaginario

De los muros que son imaginarios
penden antiguos cuadros imaginarios
irreparables grietas imaginarias
que representan hechos imaginarios
ocurridos en mundos imaginarios
en lugares y tiempos imaginarios

Todas las tardes tardes imaginarias
sube las escaleras imaginarias
y se asoma al balcón imaginario
a mirar el paisaje imaginario
que consiste en un valle imaginario
circundado de cerros imaginarios..."""

alfabeto='aábcdeéfghiíjklmnñoópqrstuúvwxyz'
ALFABETO=alfabeto.upper()
alfabeto=list(alfabeto)
alfabeto.extend(ALFABETO)

def estadisticas_frase(frase):
    saltos_de_parrafo=frase.count('\n\n')
    lines=frase.split('\n')
    parole=[]
    for i in lines:
        parole.extend(i.split(' '))
    for h in range(parole.count('')):
        parole.remove('')
    chars=[]
    for j in parole:
        chars.extend(list(j))
    palabras=len(parole)
    espacios=palabras-(len(lines)-1)+saltos_de_parrafo
    caracteres=len(hombre_imaginario)
    punctu=0
    for k in chars:
        if k not in alfabeto:
            punctu+=1
    mean=(len(chars)-punctu)/palabras
    return palabras,caracteres,mean,espacios,punctu

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))         