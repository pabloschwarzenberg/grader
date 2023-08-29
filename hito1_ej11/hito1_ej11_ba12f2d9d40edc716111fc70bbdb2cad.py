#Cajero Automático

def bills(c,x):



  billetes = c // x

  resto = c % x

  return billetes,resto



usuario = int(input("Ingrese el usuario: "))

clave = int(input("Ingrese su clave: "))



intentos = 1

saldo_cajero = 1000000

saldo_usuario = 100000

user = 10334151

passw = 1803

billetes_20 = 20000

billetes_10 = 10000

billetes_5 = 5000





while clave != passw:

  intentos += 1

  if clave == passw:

    print("clave incorrecta")

    break



  if intentos > 3:

    break



  print("clave invalida")

  clave = int(input("Ingrese de nuevo su clave: "))



if intentos > 3:

  print("tarjeta bloqueada")



if usuario == user :

  if clave == passw:

    monto = int(input("¿Cuanto quiere retirar?: "))

    if monto > saldo_usuario and monto > …
[22:27, 13/9/2021] Alvaro  Troncoso: #Adivina mi número
import random

numero_random = random.randint(1,20)

n = 1

while n<=5:

  intento = int(input("Adivina número: "))

  if intento<numero_random:

    print("Mi número es mayor")

  elif intento>numero_random:

    print("Mi número es menor")

  else:

    print("Adivinaste, mi número era",numero_random )

    break

  if n == 5:

    print("No adivinaste, mi número era",numero_random )

  n += 1      