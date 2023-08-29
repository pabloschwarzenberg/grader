import random
def ocultar_letras(palabra,cantidad):
    global h
    h = 0
    contador = 0
    lista2 = []
    while(contador != cantidad):
        posicion = random.randint(0,len(palabra)-1)
        for k in range(len(lista2)):
            if(posicion == lista2[k]):
                h = lista2[k]
                break
        while(posicion == h):
            posicion = random.randint(0,len(palabra)-1)
            for k in range(len(lista2)):
                if(posicion == lista2[k]):
                    h = lista2[k]
                    break
                
        lista_letras = list(palabra) 
        lista_letras[posicion] = "_" 
        palabra = "".join(lista_letras) 
        lista2.insert(contador,posicion)
        contador = contador + 1
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    lista2_letras = list(palabra_secreta)
    lista3 = []
    acertado = 0
    global intentos
    for p in range(len(lista2_letras)):
        if(letra == lista2_letras[p]):
            lista3.insert(p,letra)
            acertado = acertado + 1
        elif(letra == palabra_secreta):
            acertado = 1
            lista3 = lista2_letras
            break
        else:
            lista3.insert(p,palabra[p])

    if(acertado == 0):
        print("TE EQUIVOCASTE, INTENTALO DE NUEVO")
        intentos = intentos - 1
    elif(acertado >= 1 and lista2_letras == lista3):
        print("HAS ACERTADO LA PALABRA SECRETA")
        palabra = palabra_secreta
    elif(acertado >=1 and lista2_letras != lista3):
        print("HAS ACERTADO, PERO AUN NO ESTA COMPLETA")
        palabra = "".join(lista3)
    return palabra
    
if __name__ == "__main__":
    lista = ["lepidoptero","estratosfera","galeria"]
    i = random.randint(0,2)
    palabra = lista[i]
    j = len(palabra)
    cantidad = random.randint(1,j)
    palabra_secreta = palabra
    palabra = ocultar_letras(palabra,cantidad)
    intentos = 7
    while(intentos != 0):
        letra = input("Ingrese una letra o la palabra completa secreta: ")
        palabra = revisar_letra(palabra_secreta,palabra,letra)
        if(palabra == palabra_secreta):
            print("HAS GANADO")
            break
        elif(palabra != palabra_secreta):
            print("Aún faltan letras")