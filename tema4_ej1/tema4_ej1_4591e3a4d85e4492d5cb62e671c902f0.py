from random import randrange
def ocultar_letras(palabra,cantidad):
    Lista_Ltrs= list(palabra)
    Intento=[]
    while cantidad!=0:
        Random = randrange(0, len(Lista_Ltrs))
        if Random not in Intento:
            Lista_Ltrs[Random]= "_"
            Intento.append(Random)
            cantidad-=1
    Nueva_Palabra= "".join(Lista_Ltrs)
    return Nueva_Palabra

def revisar_letra(palabra_secreta,palabra,letra):
    Lista_Palabra = list(str(palabra_secreta).strip())
    Lista_Incompleta = list(str(palabra).strip())
    Letras_Secretas= []
    for i in range(len(Lista_Palabra)):
        if Lista_Palabra[i]==Lista_Incompleta[i]:
            continue
        else:
            Letras_Secretas.append(Lista_Palabra[i])
    Ubica_esp=[]
    for esp in range(len(Lista_Incompleta)):
        if Lista_Incompleta[esp]=="_":
            Ubica_esp.append(esp)
    if letra in Letras_Secretas:
        for num in Ubica_esp:
            if Lista_Palabra[num]==str(letra):
                Lista_Incompleta[num] = str(letra)
    return "".join(Lista_Incompleta)
