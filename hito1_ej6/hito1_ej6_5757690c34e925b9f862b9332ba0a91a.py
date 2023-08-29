n1 = int(input("ingrese algun numero entero: "))
n2=int(input("ingrese algun numero entero: "))
n3=int(input("ingrese algun numero entero: "))
      
maximo=max(n1, n2, n3)
minimo=min(n1, n2, n3)
n = ((n1+n2+n3)-maximo)-minimo

print(minimo, ",", n, ",", maximo)