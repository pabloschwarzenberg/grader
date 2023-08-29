#Descomponer un número
lista = []
print("Ingrese numero de 4 digitos: ")
num = input("-> ")
lista = list(num)
if len(lista) == 4:
  print(lista[0],'M','+',lista[1],'C','+',lista[2],'D','+',lista[3],'U')
elif len(lista) == 3:
  print(lista[0],'C','+',lista[1],'D','+',lista[2],'U')
elif len(lista) == 2:
  print(lista[0],'D','+',lista[1],'U')
elif len(lista) == 1:
  print(lista[0],'U')
else:
  print("Numero de digitos incorrecto")
