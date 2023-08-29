#factores primos
x=int(2);
numero=int(input(">Favor de ingresar numero a calcular factores primos:"));
while(numero!=1):
  if(numero%x==0):
    print(str(x)+"");
    numero=numero/x;
  else:
    x=x+1