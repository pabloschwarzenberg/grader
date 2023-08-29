import random

def ocultar_letras(palabra,cantidad):
    l_texto=list(palabra)

    n_aleatorio=list(range(0,len(palabra)))
    n_aleatorio=random.sample(n_aleatorio,cantidad)
    print(n_aleatorio)

    for i in n_aleatorio:
        print(i)
        l_texto[i]="_"
    palabra="".join(l_texto)
    print(palabra)
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    l_texto=list(palabra)
    for i,l in enumerate(palabra_secreta):
        print(i,l,letra)
        if l==letra:
            l_texto[i]=letra
            texto="".join(l_texto)
        else:
            pass
    return texto

if __name__ == "__main__":
    cantidad=int(input("escriba cantidad letras ocultas: "))
    palabra=str(input("escriba palabra: "))
    palabra_secreta=palabra
         