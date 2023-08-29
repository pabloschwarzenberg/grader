#Juego adivina mi número
import random

print("Bienvenido al juego ""ADIVINA MI NÚMERO")
print("Debes adivinar el número en el que piensa la computadora")
print("Para esto debes ingresar el numero que creas que es opción, si no es el correcto, la computadora dirá si este numero es mayor o menor que el que tu ingresaste.\n")
print("Debes eligir un numero entero entre el 1 y 20\n")

caca = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lista = random.randint(1, 20)
numero = random.choice(caca)

print(numero)

n = int(numero)

for i in range(5):
    w = int(input("Ingrese el número que cree que es: "))
    if w in caca:
        if w == n:
            print("Acertó el número. ¡Felicidades!\n")
            break
            
        elif w < n:
            print("El número que ingrasaste es menor al de la computadora. Intentalo de nuevo\n")

        elif w > n:
            print("El número que ingresaste es mayor al de la computadora. Intentalo de nuevo.\n")

    else:
                  print("El número ingresado no pertenece al intervalo del juego.\n")


print("El juego ha terminado. ¡Gracias por jugar!")