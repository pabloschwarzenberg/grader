#Ordenar tres números
numero1=int(input("Introduzca el primer número: "))
numero2=int(input("Introduzca el segundo número: "))
numero3=int(input("Introduzca el tercer número: "))

if((numero1<=numero2) and (numero1<=numero3)):
  nmenor=numero1
  if(numero2<=numero3):
    nmedio=numero2
    nmayor=numero3
  else:
    nmayor=numero2
    nmedio=numero3
elif((numero2<=numero1) and (numero2<=numero3)):
  nmenor=numero2
  if(numero1<=numero3):
    nmedio=numero1
    nmayor=numero3
  else:
    nmedio=numero3
    nmayor=numero1
else:
  nmenor=numero3
  if((numero1<=numero2)):
    nmedio=numero1
    nmayor=numero2
  else:
    nmedio=numero2
    nmayor=numero1
print(str(nmenor),",",str(nmedio),",",str(nmayor))