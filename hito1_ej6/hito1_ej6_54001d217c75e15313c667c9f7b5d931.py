#Ordenar tres números

numero1 = int(input("ingrese un numero: "))
numero2 = int(input("ingrese un numero2: "))
numero3 = int(input("ingrese un numero3: "))

if numero1 > numero2 and numero1 > numero3:
  nummayor = numero1
elif numero2 > numero1 and numero2 > numero3:
  nummayor = numero2
else:
  nummayor = numero3

if numero1 < numero2 and numero1 < numero3:
  nummenor = numero1
elif numero2 < numero1 and numero2 < numero3:
  nummenor = numero2
else:
  nummenor = numero3

if nummayor == numero1 and nummenor == numero2:
  nummedio = numero3
elif nummayor == numero2 and nummenor == numero1:
  nummedio = numero3
elif nummayor == numero3 and nummenor == numero1:
  nummedio = numero2
elif nummayor == numero1 and nummenor == numero3:
  nummedio = numero2
else:
  nummedio = numero1
print("orden de mayor a menor: ", str(nummenor)+","+ str(nummedio)+","+ str(nummayor))