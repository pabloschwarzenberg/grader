#Ordenar tres números
print("Ingrsa tres numeros: ")
a=int(input())
b=int(input())
c=int(input())
if a > b and b > c:
 h=c,b,a
if a > b and c > b:
 h=b,c,a
if b > a and a > c:
 h=c,a,b
if b > a and c > a:
 h=a,c,b
if c > a and a > b:
 h=b,a,c
if c > a and b > a:
 h=a,b,c
print(h)