#Juego adivina mi número
import random
num_min=1
num_max=20
jugando=True
print('HOLA,BIENVENIDO ESTE JUEGO SE LLAMA ADIVINA MI NUMERO ,USTED DISPONE DE 5 INTENTOS Y LOS NUMEROS SE GENERARAN ENTRE 1 Y 20 SUERTE.')
intentos=0
while jugando and intentos<5:  
  n_aleatorio=random.randint(1,20)
  intentos+=1
  numero=int(input("ingrese el numero que estas pensando: "))
  if n_aleatorio<numero:
    print("mi numero es menor")
  if n_aleatorio>numero:
    print("mi numero es mayor")
  if n_aleatorio!=numero and intentos==5:
    print("No adivinaste,mi numero era ",n_aleatorio)
    break
  if n_aleatorio==numero and intentos<5:
    print("Adivinaste,mi numero era ",n_aleatorio)
    break
