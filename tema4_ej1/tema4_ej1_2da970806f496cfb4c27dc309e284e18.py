import random

def ocultar_letras(palabra,cantidad):
    palabra=list(palabra)
    i=0
    while i<cantidad:
        x=random.randint(0,len(palabra)-1)
        if palabra[x]!="_":
            palabra[x]="_"
            print(palabra)
            i+=1
        else:
            continue
    nueva_palabra="".join(palabra)
    return nueva_palabra

def revisar_letra(palabra_secreta,palabra,letra):
    palabra=list(palabra)
    palabra_secreta=list(palabra_secreta)
    
    if letra in palabra:
        for i in range(0,len(palabra_secreta)):
            if (palabra_secreta[i]=="_") and (palabra[i]==letra):
                palabra_secreta[i]=letra
    palabra_secreta="".join(palabra_secreta)
    return palabra_secreta

palabras=["lepidoptero","casa","perro","gato","auto"]
palabra=palabras[random.randint(0,len(palabras)-1)]
cantidad=random.randint(0,len(palabra))
palabra_secreta=ocultar_letras(palabra,cantidad)



if __name__=="__main__":
    intentos=0
    while intentos<7 and (palabra_secreta not in palabra):
        print(palabra_secreta)
        letra=input("Escoja una letra del abecedario:")
        palabra_secreta=revisar_letra(palabra_secreta,palabra,letra)
        intentos+=1
    if palabra_secreta in palabra:
        print(palabra)
        print("FELICIDADES, HAS GANADO EL JUEGO!")
    else:
        print("Lo sentimos, se han acabado tus turnos, la palabra secreta es:",palabra)

