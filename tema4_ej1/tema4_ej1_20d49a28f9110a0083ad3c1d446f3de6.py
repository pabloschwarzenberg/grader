import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    P_oculta = list(palabra)
    for indice in letras_ocultas:
        P_oculta[indice] = "_"
    return "".join(P_oculta)

def revisar_letra(P_secreta, P_mostrada, letra):
    nueva_palabra_mostrada = list(P_mostrada)
    for indice, caracter in enumerate(P_secreta):
        if caracter == letra:
            nueva_palabra_mostrada[indice] = letra
    return "".join(nueva_palabra_mostrada)

if __name__ == "__main__":
    P_secretas = ["lepidoptero", "mariposa", "oruga", "pupa", "antenas"]
    P_secreta = random.choice(P_secretas)
    L_mostradas = random.randint(1, len(P_secreta))
    P_mostrada = ocultar_letras(P_secreta, L_mostradas)

    print("¡Bienvenido al juego de adivinar la palabra!")
    print("Tienes hasta 7 intentos para adivinar la palabra.")
    print("La palabra mostrada es:", P_mostrada)

    intentos = 0
    while intentos < 7:
        entrada = input("Ingresa una letra o arriésgate a decir la palabra completa: ")
        if len(entrada) == 1:
            P_mostrada = revisar_letra(P_secreta, P_mostrada, entrada)
            print("La palabra mostrada es:", P_mostrada)
        else:
            if entrada == P_secreta:
                print("¡Felicidades! Adivinaste la palabra correcta.")
                break
            else:
                print("Lo siento, esa no es la palabra correcta.")
        intentos += 1
    else:
        print("¡Perdiste! Se te acabaron los intentos. La palabra secreta era:", P_secreta)