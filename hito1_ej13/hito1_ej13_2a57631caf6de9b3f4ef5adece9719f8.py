#Factores Primos
numero=int(input("ingrese numero:"))
x=int(2)
while(numero!=1):
  if(numero%x==0):
    print(str(x));
    numero=numero/x;
  else:
      x=x+1