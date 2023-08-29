import random
lista_palabras=["camion", "casa", "perro", "paralelepipedo", "supercalifragilisticoespialidoso", "megalodonte", "esquisofrenia", "gato", "mikasa"]


def ocultar_letras(palabra,cantidad):
    cantidad=int(cantidad)
    i=0
    palabra2=palabra
    while i<=cantidad:
        espacio=random.randrange(0,len(palabra))
        l_palabra=list(palabra)
        for a in range(len(l_palabra)):
            l_palabra[espacio]="_"
            palabra="".join(l_palabra)
        i+=1
    return palabra

def revisar_letra(palabra,palabra_secreta,letra):
    palabra=list(palabra)
    palabra_secreta=list(palabra_secreta)
    if palabra.count(letra)==0:
        return palabra_secreta
    else:
        if palabra_secreta.count(letra)==0:
            palabra_secreta.insert(palabra.index(letra),letra)
            palabra_secreta.pop(palabra.index(letra)+1)
            return palabra_secreta
        else:
            if palabra.count(letra)>1:
                n=palabra.index(letra)
                if palabra_secreta[n]==palabra[n]:
                    n=n+1
                    palabra_secreta.insert(palabra.index(letra,n),letra)
                    palabra_secreta.pop(palabra.index(letra,n)+1)
                else:
                    palabra_secreta.insert(palabra.index(letra),letra)
                    palabra_secreta.pop(palabra.index(letra)+1)
        palabra_secreta="".join(palabra_secreta)
        return palabra_secreta
        
if __name__ == "__main__":
     palabra=random.choice(lista_palabras)

         