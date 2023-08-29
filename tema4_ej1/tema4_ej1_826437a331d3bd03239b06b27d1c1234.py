import random

def revisar_palabra(self):
    if self == juego.palabra_secreta:
        print("GANASTE!")
        return True
    else:
        return False


def ocultar_letras(palabra, cantidad):
    lista = []
    for j in palabra:
        lista.append(j)
        #print(lista)
    for i in range(cantidad):
        espacio = random.randint(0, len(palabra)-1)
        lista[espacio] = "_"
    palabra = "".join(lista)
    #print(palabra)
    return palabra


def revisar_letra(palabra_secreta, palabra, letra):
    añadir_letra = True
    guiones = [i for i, c in enumerate(palabra) if c == "_"]
    #print(guiones)
    palabra = list(palabra)
    for i in guiones:
        i = int(i)
        if palabra_secreta[i] == letra:
            palabra[i] = letra
            añadir_letra = False
    if añadir_letra:
        juego.letras_erroneas.append(letra.upper())
    palabra = "".join(palabra)
    return palabra

class juego:
    @staticmethod
    def jugar():
        while juego.vidas > 0:
            letra = str(input("Ingrese una palabra o letra:"))
            if len(letra) > 1:
                if revisar_palabra(letra):
                    break
                else:
                    juego.vidas -= 1
                    print("Intente de nuevo")
            else:
                juego.palabra = revisar_letra(juego.palabra_secreta, juego.palabra, letra)
                print(juego.palabra)
                print("Letras Erroneas: ", juego.letras_erroneas)
            if revisar_palabra(juego.palabra):
                break

    palabras_posibles= ["cocos", "huevos", "bolas", "cola", "lepidoptero", "murcielago", "mañana"]
    vidas = 7
    palabra_secreta = random.choice(palabras_posibles)
    #print(palabra_secreta)
    cantidad = int(len(palabra_secreta)//1.5)
    #print(cantidad)
    palabra = ocultar_letras(palabra_secreta, cantidad)
    letras_erroneas = []

if __name__ == "__main__":
    juego.jugar()

         