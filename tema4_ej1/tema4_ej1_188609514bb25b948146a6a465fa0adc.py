import random

lista_secreta = ["hipopotamo", "electromagnetismo", "pasto", "jurisprudencia", "dicotomia", "hola", "paralelepidedo", "naufrago", "felicidad", "antidepresivos", "jurisdiccion"]
spalabra  = lista_secreta[random.randint(0,len(lista_secreta)-1)]

def ocultar_letras(spalabra, cantidad) :

    while (len(spalabra) < cantidad) or (cantidad < 1):
        print("Cantidad de caracteres a ocultar mayor a cantidad de letras. Ingrese cantidad de nuevo")
        cantidad = int(input("Cantidad: "))
    lista_spalabra =[]
    for i in spalabra :
        lista_spalabra.append(i)
    i = 0
    while i < cantidad :
        a = lista_spalabra.index(lista_spalabra[random.randint(0, len(lista_spalabra)-1)])
        if lista_spalabra[a] != "_" :
            lista_spalabra[a] = "_"
        else :
            i -= 1
        i += 1
    palabra = "".join(lista_spalabra)

    return palabra

def revisar_letra(palabra_secreta, palabra) :

    vidas = 7

    while vidas > 0 :
        letra = str(input("Letra (o palabra):"))
        if len(letra) == 0 :
            print("por favor ingrese mas de 0 caracteres")
            vidas += 1
        elif len(letra) == 1 :
            if letra in palabra_secreta :
                lista_palabra = list(palabra)
                lista_palabra_secreta = list(palabra_secreta)
                i = 0
                for i in (range(len(lista_palabra_secreta))) :
                    if letra == lista_palabra_secreta[i] :
                        lista_palabra[i] = letra
            palabra = "".join(lista_palabra)
            print(palabra)

        else :
            if letra == palabra_secreta :
                return  "Adivinaste la palabra"
            else :
                return "Perdiste"
        vidas -= 1

    if vidas == 0:
        return "Perdiste"

cantidad = int(input("Cantidad: "))
palabra_secreta = spalabra
palabra = ocultar_letras(spalabra, cantidad)

    #print(palabra_secreta)
print(palabra)