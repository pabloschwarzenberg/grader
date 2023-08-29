from os import system
system ("cls")
def contestar_llamada(numero, hora):
    # Verificar si la llamada ocurre entre 00:00 y 07:00
    if hora >= 0 and hora <= 7:
        return "CONTESTAR"
    # Verificar si la llamada ocurre antes de las 14:00, excepto si el número termina en 909
    elif hora < 14 and not str(numero)[-3:] == "909":
        return "NO CONTESTAR"
    # Verificar si la llamada ocurre entre 17:00 y 19:00, excepto si el número comienza por 877
    elif hora >= 17 and hora <= 19 and not str(numero)[0:3] == "877":
        return "CONTESTAR"
    # No contestar la llamada en cualquier otro caso
    else:
        return "NO CONTESTAR"

# Solicitar al usuario el número telefónico y la hora de la llamada
numero = int(input("Ingrese número telefónico: "))
hora = int(input("Ingrese hora de la llamada (formato 24 horas): "))

# Determinar si se debe contestar o no la llamada y mostrar el resultado
resultado = contestar_llamada(numero, hora)
print("Resultado:", resultado)
