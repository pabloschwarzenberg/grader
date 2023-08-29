#Factores Primos
a= int(2);
numero = int(input("Ingresar numero a calcular: "));
 
while (numero!=1):

 if (numero%a==0):
  print(str(a)+" ");
  numero=numero /a;
 else:
  a=a+1