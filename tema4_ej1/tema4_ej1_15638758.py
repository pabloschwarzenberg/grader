import random

def ocultar_letras(palabra,cantidad):
    cambiados=0
    lista=[]
    for i in palabra:
        lista.append(i)
    while cantidad>cambiados:
        pos=random.randint(0,len(palabra)-1)
        if lista[pos]!="_":
            lista[pos]="_"
            cambiados+=1
    palabra=""
    for i in lista:
        palabra+=i
    return palabra

def revisar_letra(palabra,palabra_secreta,letra):
    lista=[]
    lista2=[]
    for i in palabra:
        lista.append(i)
    for i in palabra_secreta:
        lista2.append(i)
    if len(letra)==1:
        for i in range(len(lista)):
            if letra==lista[i]:
                lista2[i]=letra
    else:
        if letra==palabra:
            return letra
    palabra_secreta=""
    for i in lista2:
        palabra_secreta+=i
    return palabra_secreta

if __name__ == "__main__":
    lista = ["paraguas","armadillo","botella","sindicato","arroba","lamentable","ecuestre","sabanas","calavera",
             "pinkfloyd","alinear","teclado","farmaceutico","jirafa","teletubbie","estreptococo","strogonoff",
             "condorito","programar","laguna","indigena","chile","jabon","jamon","laberinto","colgado","ganaste",
             "fluidos","cruzadas","cienpies","lubricar","crucero","bolivia","no","tiene","ni","nunca","tendra","mar"]

    palabra=random.choice(lista)
    mostrar=random.randint(1,len(palabra))
    palabra_oculta=ocultar_letras(palabra,mostrar)
    while True:
        print(palabra_oculta)
        adivina=(str(input("Adivine una letra o la palabra completa")))
        palabra_oculta=revisar_letra(palabra,palabra_oculta,adivina)
        if "_" not in palabra_oculta:
            print("Listo!")
            break
         