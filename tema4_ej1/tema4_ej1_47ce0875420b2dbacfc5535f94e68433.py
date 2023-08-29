import random
def ocultar_letras(palabra,cantidad):
    i=0
    long_p_s=len(palabra)
    palabra=list(palabra)
    while i<cantidad+1:
        letra_oculta=random.randint(0,long_p_s-1)
        palabra.pop(letra_oculta)
        palabra.insert(letra_oculta,"_")
        i=i+1
    palabra="".join(palabra)
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    j=0
    palabra_secreta=list(palabra_secreta)
    long_p_s=len(palabra_secreta)
    palabra=list(palabra)
    long_p=len(palabra)
    while j<long_p_s:
        print(palabra_secreta[j],palabra[j])
        if palabra_secreta[j]==letra:
            palabra.pop(j)
            palabra.insert(j,letra)
        j=j+1
    palabra="".join(palabra)
    return palabra

palabras=["bateria","radio","camarote","hueso","paralelepipedo","carifragilisticoespialidoso"]
if __name__ == "__main__":
    palabra_secreta=random.choice(palabras)
    palabra_secreta=list(palabra_secreta)
    long_p_s=len(palabra_secreta)
    palabra=ocultar_letras(palabra_secreta,random.randint(1,long_p_s))
    print("Tu palabra es",palabra)
    a=1
    while a<8:
        resp=input("¿Se quiere arriesgar con una palabra?")
        if resp=="si":
            turno=input("¿Cúal palabra cree que es?: ")
            palabra_secreta="".join(palabra_secreta)
            if turno==palabra_secreta:
                a=10
            else:
                print(palabra,palabra_secreta)
                print("Lo lamento esa no es la palabra correcta, intentelo nuevamente")
                a=a+1
        elif resp=="no":
            letra=input("¿Que letra cree que tenga la palabra?: ")
            revisar_letra(palabra_secreta,palabra,letra)
            palabra_secreta="".join(palabra_secreta)
            if palabra==palabra_secreta:
                a=10
            else:
                print(palabra)
                print("Aun no logras adivinar la palabra completa, sigue intentandolo")
                a=a+1
        else:
            print("Tienes que responder si/no")
    if a==10:
        print("Felicidades encontraste la palabra",palabra_secreta)
    elif a==8:
        print("Para la otra tendras mas suerte")
    pass