#Factores Primos
nu = int(2);
x = int(input("Ingresa numero"))
while (x != 1):
  if (x % nu == 0):
    print(str(nu)+" ");
    x=x/nu;   
  else:
     nu = nu+1;
      