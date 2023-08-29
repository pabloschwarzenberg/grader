import random
#primero las definiciones de función
def ocultar_letras(palabra,cantidad):
            #global palabra1
            #esto no es necesario que sea global
            palabra1=list(palabra)
            c=0
            if cantidad>len(palabra1):
                   print("esa cantidad de letras no es válida")
                   return
            while c < cantidad:
              x=random.randint(0,len(palabra1)-1)
              if palabra1[x]!="_":
                 palabra1[x]="_"
                 c+=1
            #cuando terminas de ocultar las letras retornas la palabra cambiada
            return "".join(palabra1)

def revisar_letra(palabra_secreta,palabra,letra):
    palabra=list(palabra)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i]==letra and palabra[i]=="_":
            #dentro de la función no debieran haber print que informen el resultado
            #la función debe retornar un valor que es usado por el que la llama
            #para imprimir información o bifurcar el programa
            palabra[i]=letra
    return "".join(palabra)

if __name__=="__main__":

    palabras="hola","chao","rapunzel","fuego","bombero","sacrilegio","hiroshima","destruccion"
    n=random.randint(0,7)
    intentos=7

    palabra_secreta= palabras[n]
    f=len(palabra_secreta)-1
    print("¿Cuántas letras deseas ocultar? Escoge un número entre 1 y",f)
    q=int(input(""))
    palabra1=ocultar_letras(palabra_secreta,q)

    while intentos> 0 and palabra_secreta!=palabra1:
        print("tienes",intentos,"intentos")
        print (palabra1)
        l=input("¿que letra?: ")
        antes=palabra1.count("_")
        palabra1=revisar_letra(palabra_secreta,palabra1,l)
        adivina=palabra1.count("_")
        if adivina<antes:
            print("Has adivinado una letra!")
        else:
            print("Esa letra no es correcta")
            intentos -=1

    if palabra_secreta==palabra1:
        print("¡Felicidades, has ganado! La palabra era", palabra_secreta)
    if intentos==0:
        print("Lo siento, te has quedado sin intentos")