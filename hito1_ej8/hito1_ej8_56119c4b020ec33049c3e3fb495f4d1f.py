#Descomponer un número
lista = []
numero = input("ingrese un numero: ")
for i in numero:
  num = i
  lista.append(num)

if len(lista) == 4:
  print(lista[0]+"M","+",lista[1]+"C","+",lista[2]+"D","+",lista[3]+"U")

elif len(lista) == 3:
  print(lista[0]+"C","+",lista[1]+"D","+",lista[2]+"U")

elif len(lista) == 2:
  print(lista[0]+"D","+",lista[1]+"U")

elif len(lista) == 1:
  print(lista[0]+"U")