#adivina la palabra
import random
lista_de_palabras = ["piano", "guitarra", "decodificar", "automovil", "matematicas", "avioneta", "computador", "programacion", "atardecer", "ciudad", "velocidad", "lujos", "bateria", "partitura", "videojuego", "amigos", "destruccion", "lepidoptero"]
palabra_secreta = random.choice(lista_de_palabras)
intentos = 7
cantidad = random.randint(3, len(palabra_secreta))

def ocultar_letras(palabra,cantidad):
    posicion = random.randint(1, len(palabra))
    caracter = "_"
    cantidad = cantidad
    while cantidad > 0:
        posicion = random.randint(1, len(palabra))
        palabra = palabra[:posicion] + caracter + palabra[posicion+1:]
        cantidad -= 1
    return palabra

def revisar_letra(palabra_secreta, palabra, letra):
    letra = letra
    for i in range(1, len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            palabra = palabra.replace("_", letra)
    return palabra

print("Bienvenido a adivina la palabra.")
print("Intenta adivinar la palabra completa o intenta letra por letra")
palabra_secreta_oculta = ocultar_letras(palabra_secreta, cantidad)
print("Tu palabra es:", palabra_secreta_oculta)

while intentos > 0:
    
    guess = str(input("Adivina la palabra: "))
    guess = revisar_letra(palabra_secreta, palabra_secreta_oculta, guess)
    intentos -= 1
    print(guess)
    
    
if guess == palabra_secreta:
    intentos = 0
    print("Ganaste! La palabra era:", palabra_secreta)
elif "_" not in palabra_secreta:
    intentos = 0
    print("Ganaste! La palabra era:", palabra_secreta)
    
print("Perdiste :(. La palabra era:", palabra_secreta)
