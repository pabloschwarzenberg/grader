numero = input("Ingrese un numero de maximo 4 digitos: ")

if len(numero) > 4:
  numero = input("Reingrese el numero: ")

while len(numero) != 4:
  numero = "0" + numero

lista = ["M", "C", "D", "U"]
num = []

for a in numero:
  num.append(a)

s = ""
for a in range(len(num)):
  if a < len(num) - 1:
    s += num[a] + lista[a] + " + "
  elif a == len(num) -1:
    s += num[a] + lista[a]

print(s)