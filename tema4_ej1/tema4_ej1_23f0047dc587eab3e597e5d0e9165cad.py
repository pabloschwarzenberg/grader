import random

lista=["paulo","nicolas","trinidad","ariel","rocio"]
x=random.randint(0,4)
palabra_secreta=lista[x]
palabra=lista[x]
y=int(len(palabra))
cantidad=random.randint(1,y)

e=random.randint(1,y)
posicion=lista[e]

def ocultar_letras(palabra, cantidad):

    for i in range(len(palabra)):
        palabra[i]=palabra[i].replace(posicion,"_")
        
    return palabra

letra=str(input("Ingrese letra: "))
intentos=6

def revisar_letra(palabra_secreta,palabra,letra):

    if letra==




        intentos-=1

    else:
        
        intentos-=1

if __name__ == "__main__":
    pass
         