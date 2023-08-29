
import random

intentosRealizados = 1

print("Nombre Jugador :")
miNombre = input()

numero = random.randint(1, 20)
print('Inserte Numero al Azar del 1 al 20:')

while intentosRealizados < 6:
     print('Intenta adivinar.')
     numero2 = input()
     numero2 = int(numero2)

     intentosRealizados = intentosRealizados + 1

     if numero2 < numero:
         print('Más arriba') 

     if numero2 > numero:
         print('Más Abajo.')

     if numero2 == numero:
         break

if  numero2 == numero:
     numero= str(numero)
     print('Adivinaste, mi número era:'+ numero)
elif numero2 != numero:
     numero = str(numero)
     print('No adivinaste, mi número era:' + numero)
if __name__ == "__main__":
