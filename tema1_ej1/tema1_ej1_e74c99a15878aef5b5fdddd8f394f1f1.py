while True:
  n=int(input("Ingrese el número límite:"))
  if n>=1:
    break
  else:
    print("Debe ingresar un número entero positivo")
s=n*(n+1)/2
print("La suma de los ",n," primeros numeros naturales es ",s)