x = int(2)
n = int(input("favor de ingresar al numero a calcular factores primos:"))
while (n != 1):
  if n %x == 0:
    print(str(x)+" ")
    n = n / x
  else:
    x = x+1