#Juego adivina mi número
import random
estimacion=0
intentosRealizados = 0
num=0

print('¡Hola! ¿Cómo te llamas?')
miNombre = input()

 
numeroo = random.randint(1, 20)
numero = int(numeroo)
print('Bueno, ' + miNombre + ', estoy pensando en un número entre 1 y 20.')

while intentosRealizados < 6:
  
  intentosRealizados = intentosRealizados + 1
  if __name__=="__main__":
   num = int(input("Intenta adivinar"))

  if num < numeroo:
    print('Mi numero es mayor.') # Hay ocho espacios delante de print.
    
  if num > numeroo:
    print('Mi numero es menor.')
    
  if num == numeroo:
    break
    
if num == numeroo:
  intentosRealizados = str(intentosRealizados)
  print('¡Adivinaste, ' + miNombre + '! ¡Has adivinado mi número en ' + intentosRealizados + ' intentos, el cual era: ', numero)

if num != numeroo:
  numeroo = str(numeroo)
  print('Pues no pudiste. El número que estaba pensando era: ', numero)
      