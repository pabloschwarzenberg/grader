#Factores Primos
x= int(2)
numero_p=int(input("Ingrese numero: "))
while(numero_p != 1):
  if (numero_p % x == 0 ):
    print(str(x) + "")
    numero_p=numero_p / x
  else:
    x = x +1   