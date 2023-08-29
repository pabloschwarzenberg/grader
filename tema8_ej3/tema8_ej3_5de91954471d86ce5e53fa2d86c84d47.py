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

def estadisticas_frase(frase):
    letras=['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','ñ','o','p','q','r','s','t','u','v','w','x','y','z'
           'á','é','í','ó','ú','á']
    n_pal=len(frase.split())
    n_carac=len(frase)
    suma_prom=0
    n_espacios=frase.count(' ')
    n_punt=0
    for posible_pal in frase.split():
        largo_posible=len(posible_pal)
        if largo_posible>0:
            posible_pal=posible_pal.lower()
            puntuaciones=0
            for c in posible_pal:
                if c not in letras:
                    puntuaciones+=1
                    print(c)
            largo=largo_posible-puntuaciones
            suma_prom+=largo
            n_punt+=puntuaciones
    l_prom=suma_prom/n_pal
    return n_pal,n_carac,l_prom,n_espacios,n_punt

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         