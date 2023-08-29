#Descomponer un número
numero = int(input())
digitos = [0,0,0,0]
inicio = 0
if numero < 1000:
  inicio = 1
elif numero < 100:
  inicio = 2
elif numero < 10:
  inicio = 3

numero = str(numero)
numero = list(numero)
for x in range(inicio):
  numero.insert(0,"0")
  
print(numero[0] + "M+" + numero[1] + "C+" + numero[2] + "D+" + numero[3] + "U")