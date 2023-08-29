#Descomponer un número
while True:
   numero = input("escriba un numero ")

   if (len(numero) <= 4):
      break

if len(numero) == 4: resultado = numero[0:1] + "M+" + numero[1:2] + "C+" + numero[2:3] + "D+" + numero[3:4] + "U"
elif len(numero) == 3: resultado = numero[0:1] + "C+" + numero[1:2] + "D+" + numero[2:3] + "U"
elif len(numero) == 2: resultado = numero[0:1] + "D+" + numero[1:2] + "U"
elif len(numero) == 1: resultado = numero[0:1] + "U"

print(resultado)