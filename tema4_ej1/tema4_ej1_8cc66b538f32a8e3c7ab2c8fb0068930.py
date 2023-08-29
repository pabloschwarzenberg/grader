list_palabras=["hola","chao","saludo"]
import random
palabra=list_palabras[random.randint(0,2)]
palabra_secreta=palabra

def ocultar_letras(palabra,cantidad):
    palabra=list(palabra)
    a=1
    while a<=cantidad:
        i=random.randint(0,len(palabra)-1)
        if palabra[i]!="_":
            palabra.pop(i)
            palabra.insert(i,"_")
            a=a+1
        else:
            continue
    palabra="".join(palabra)
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    if letra in palabra_secreta:
        while palabra.count(letra)!=palabra_secreta.count(letra):
            a=0
            while a<len(palabra):
                if palabra[a]=="_":
                    if palabra_secreta[a]==letra:
                        x=list(palabra)
                        x.pop(a)
                        x.insert(a,letra)
                        palabra="".join(x)
                a=a+1
        return palabra
        

if __name__ == "__main__":
    cantidad=int(input("cantidad de letras: "))
    print(ocultar_letras(palabra,cantidad))
    letra=input("Ingresa letra: ")
    print(revisar_letra(palabra_secreta,palabra,letra))
