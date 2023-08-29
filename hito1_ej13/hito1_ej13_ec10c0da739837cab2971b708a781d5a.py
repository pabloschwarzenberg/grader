#Factores Primos
x=2
numero=int(input("Ingrese un numero: "))
while(numero != 1):
  if(numero%x == 0):
    print(str(x) + " ")
    numero=numero/x
  else:
    x=x+1