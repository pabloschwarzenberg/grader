#FACTORES PRIMOS
nu=int(2);
x=int(input(">Favor de ingresar el numero a calcular factor primos:"));
    
while (x!=1):
    if(x%nu==0):
         print(str(nu)+" ");
         x=x/nu;

    else:
         nu=nu+1;
