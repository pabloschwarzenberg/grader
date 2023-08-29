#suma de numeros naturales 
while True:
 try:
    n=int(input("Ingrese un numero natural: "))

    if n>1:
       break

    else:
      print("Debe ingresar un entero positivo")

 except ValueError:
  print("Debe escribir un numero entero valido")

suma=n*(n+1)/2
print("La suma desde 1 hasta ", n, "es", suma)