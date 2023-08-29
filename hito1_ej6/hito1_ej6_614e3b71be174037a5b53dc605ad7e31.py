#Ordenar tres números
valorA=int(input("Escrba el primer valor: "))
valorB=int(input("Escrba el segundo valor: "))
valorC=int(input("Escrba el tercer valor: "))

if (valorA<=valorB<=valorC):
  print("el orden de menor a mayor es:",valorA,",",valorB,",",valorC,)

elif (valorA<=valorC<=valorB):
  print("el orden de menor a mayor es:",valorA,",",valorC,",",valorB,)

elif (valorB<=valorA<=valorC):
  print("el orden de menor a mayor es:",valorB,",",valorA,",",valorC,)

elif (valorB<=valorC<=valorA):
  print("el orden de menor a mayor es:",valorB,",",valorC,",",valorA,)

elif (valorC<=valorA<=valorB):
  print("el orden de menor a mayor es:",valorC,",",valorA,",",valorB,)

elif (valorC<=valorB<=valorA):
  print("el orden de menor a mayor es:",valorC,",",valorB,",",valorA,)