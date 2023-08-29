from random import choice

def ocultar_letras(palabra,cantidad):
    palabra = list(palabra)
    num_pal = list(range(len(palabra)))
    for i in range(1,cantidad+1):
        x = int(choice(num_pal))
        if palabra[x]=="_":
            while palabra[x]=="_":
                x = int(choice(num_pal))
        if palabra[x]!="_":
            palabra[x]="_"
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    p = 0
    palabra = list(palabra)
    for i in palabra_secreta:
        if letra == i:
            palabra[p]=i
            p+=1
        else:
            p+=1
            continue
        k = ""
        for e in palabra:
            k += e
    return k

if __name__ == "__main__":
    lista_de_palabras = ["camara","chimenea","erupcion","apagado","volcan",
                     "gases","materialoes","pequeños","pulgadas","vapor",
                     "agua","casa","acciones","colegio","festividades","comida",
                     "paralelepipedo"]

    selec_pal = choice(lista_de_palabras)
    letras = list(range(len(selec_pal)))
    letras.remove(0)
    letras.append(len(selec_pal))
    selec_num = choice(letras)
    pal_oculta = ocultar_letras(selec_pal,selec_num)

    for i in range(len(pal_oculta)):
        print(pal_oculta[i],end=" ")
    print("")

    while True:
        probar = str(input("Ingrese una letra:"))
        testeo = revisar_letra(selec_pal,pal_oculta,probar)

        for i in range(len(testeo)):
            print(testeo[i],end=" ")
        print("")

        for u in testeo:
            if u=="_":
                break
        if u!="_":
            break
         