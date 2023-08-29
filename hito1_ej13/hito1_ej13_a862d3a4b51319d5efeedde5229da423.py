#Factores Primos
x = int(2) 
numeroP = int(input("Ingrese el numero: ")) 
while(numeroP != 1): 
  if (numeroP % x == 0 ):
    print(str(x) + "") 
    numeroP = numeroP / x 
  else:
    x = x + 1