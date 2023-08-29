#Escribe un programa que reciba tres números enteros y los imprima ordenados de menor a mayor, separados por una coma.
a=int(input("Escriba un numero entero "))
b=int(input("Escriba un segundo numero entero "))
c=int(input("Escriba un tercer numero entero "))
if(a>b):
  aux=a
  a=b
  b=aux
if(b>c):
  aux=b
  b=c
  c=aux
if(c>a):
  aux=c
  c=a
  a=aux
  print(c,",",b,",",a)