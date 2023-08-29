import random as rnd
aleatorio_palabras = rnd.randint(0, 3)
palabras_secretas= ["hola", "flores","pedro","lepidoptero"]


palabra= palabras_secretas[aleatorio_palabras]
largo=len(palabra)

aleatorio_ocultar = rnd.randint(1, largo-1)

def ocultar_letras(palabra, cantidad):
    i=0
    palabra_oculta=""
    largo = int(len(palabra))
    while i < largo:
        if i < cantidad:
            palabra_oculta+= "_"
        else:
            palabra_oculta+=palabra[i]
        i+=1
    return palabra_oculta



def revisar_letra(palabra_secreta, palabra, letra):
    i=0
    list=""

    for x in palabra_secreta:
            while i < len(palabra):
                if palabra[i] == "_" and palabra_secreta[i]==letra:
                    list += letra[0]
                else:
                    list += palabra[i]
                i += 1



    return list


if __name__ == "__main__":
    print(aleatorio_palabras)
    print(palabra)
    print(largo)
    print(aleatorio_ocultar)
    a=ocultar_letras(palabra,aleatorio_ocultar)
    print(a)
    letra=input("Ingresar letra")
    mostrar=revisar_letra(palabra,a,letra)


    print(mostrar)
    pass

