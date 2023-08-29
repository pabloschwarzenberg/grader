#Factores Primos
numero=int(input("ingrese número:"))
x=2
while (numero!=1):
  if(numero%x==0):
    print(x)
    numero=numero/x;
  else:
    x=x+1