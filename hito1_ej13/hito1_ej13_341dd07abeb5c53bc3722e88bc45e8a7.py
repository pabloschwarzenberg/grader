#Factores Primos
a=int(input("Ingrese un numero entero: "))
b=2

while b<=a:
  if a%b==0:
    print(b)
    a = a/b
  else:
    b+=1





