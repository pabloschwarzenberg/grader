from random import randint as elegir

def ocultar_letras(palabra,cantidad):
    palabra=str(palabra)
    cantidad=int(cantidad)
    palabra=list(palabra)
    j=0
    while j<=cantidad:
        palabra[elegir(0,len(palabra)-1)]="_"
        j+=1
    string=""
    i=0
    while i<len(palabra):
        string=string+palabra[i]
        i+=1
    palabra=string
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    cambio=""
    if letra in palabra_secreta:
        palabra=list(palabra)
        palabra_secreta=list(palabra_secreta)
        i=0
        while i<len(palabra):
            if palabra_secreta[i]==letra:
                palabra[i]=letra
            i+=1
        for carac in palabra:
            cambio=cambio+carac
            palabra=cambio
        return palabra
         