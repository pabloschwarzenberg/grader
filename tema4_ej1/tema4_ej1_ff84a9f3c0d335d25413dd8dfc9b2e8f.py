import random
def ocultar_letras(palabra_secreta,cantidad):
    palabra=list(palabra_secreta)
    i=1
    while i<=cantidad:
        a=random.randint(0,len(palabra)-1)
        if palabra[a]!="_":
            palabra[a]="_"
            i=i+1
        else:
            i=i+0
    palabra="".join(palabra)
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    if len(letra)==len(palabra_secreta):
        if letra==palabra_secreta:
            return "Ganaste!"
        else:
            palabra="".join(palabra)
            return palabra
    else:
        palabra_secreta=list(palabra_secreta)
        palabra=list(palabra)
        coincidencias=[]
        for i in range(len(palabra_secreta)):
            if palabra_secreta[i]==letra:
                coincidencias.append(i)
        if coincidencias==[]:
            palabra="".join(palabra)
            return palabra
        else:
            for i in coincidencias:
                palabra[i]=letra
            palabra="".join(palabra)
            palabra_secreta="".join(palabra_secreta)
            if palabra==palabra_secreta:
                return "Ganaste!"
            else:
                return palabra

if __name__ == "__main__":
    lista=["lepidoptero","carpintero","ornitorrinco","enjambre","helicoptero","pterodactilo"]
    palabra_secreta=random.choice(lista)
    cantidad=random.randint(1,len(palabra_secreta))
    palabra=ocultar_letras(palabra_secreta,cantidad)
    print(palabra)

    i=1
    while i<=7:
        letra=input("Ingrese letra: ")
        print(revisar_letra(palabra_secreta,palabra,letra))
        if revisar_letra(palabra_secreta,palabra,letra)=="Ganaste!":
            break
        else:
            palabra=revisar_letra(palabra_secreta,palabra,letra)
            i=i+1