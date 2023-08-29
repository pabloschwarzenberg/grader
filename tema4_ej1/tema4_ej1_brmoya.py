import random
def ocultar_letras(palabra,cantidad):
    lista=list(palabra)
    i=0
    while i<cantidad:
        posicion = random.randint(0, len(palabra) - 1)
        if lista[posicion]=="_":
            continue
        else:
            del lista[posicion]
            lista.insert(posicion, "_")
            i+=1
    return lista
    
def revisar_letra(palabra_secreta,palabra,letra):
    palabra_lista=list(palabra)
    for i in palabra_lista:
        if letra==i:
            posicion=palabra_lista.index(i)
            del palabra_secreta[posicion]
            palabra_secreta.insert(posicion,letra)
            posicion+=1
        else:
            continue
    return palabra_secreta


if __name__ == "__main__":
    lista_secreta=["perro","helicoptero","benjamin"]
    palabra=random.choice(lista_secreta)
    letra_secreta=ocultar_letras(palabra,random.randint(1,len(palabra)))
    print(letra_secreta)
    letra=str(input("ingrese una letra: "))
    print(revisar_letra(letra_secreta,palabra,letra))
    i=0
    while i<7:
        if i==6:
            print("se le acabaron las vidas")
            break
        else:
            letra = str(input("ingrese una letra: "))
            print(revisar_letra(letra_secreta, palabra, letra))
            i+=1
         