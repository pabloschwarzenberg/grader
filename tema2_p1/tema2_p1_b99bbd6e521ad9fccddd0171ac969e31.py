# por favor escribe aquí tu función
lista=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,67,61,72,73,79,83,89,97]
def es_primo(numero):
    c=0
    for i in range(len(lista)):
        x=i-1
        if numero==lista[x]:
             c = 1
    return c==1