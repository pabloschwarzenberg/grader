import random 
def ocultar_letras2(palabra,cantidad):
    lista_palabra=list(palabra) #transforma la palabra en una lista
    letras_borradas=list(range(len(palabra)))
    if cantidad<=len(palabra):
        for i in range(0,cantidad):
            x=random.choice(letras_borradas)
            lista_palabra[x]="_"
            letras_borradas.remove(x)
        p="".join(lista_palabra)
        return p
    return "Utilizar una cantidad de letras menor o igual a la de la palabra"



def revisar_letra(palabra_secreta,palabra,letra):
    if palabra == palabra_secreta:
        return "la palabra secreta es: " + palabra_secreta 
    if letra in palabra_secreta:
        lista_palabra = list(palabra)
        lista_secreta = list(palabra_secreta)
        for index, letter in enumerate(lista_secreta):
            if letter==letra:
                lista_palabra[index] = letra
        palabra_="".join(lista_palabra)
        return palabra_
    return("Esta letra no está en la palabra")

if __name__ == "__main__":
    pass

         