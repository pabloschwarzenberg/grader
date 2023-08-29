def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    return suma
numero = int(input("Ingresa el número: "))
print("La suma de sus divisores es: ")
print(suma_divisores(numero))
n=numero
x=1
c=0
while x<=n:
  if n % x == 0:
    c=c+1
  x=x+1
if c==2:
    print(f"{numero} ES PRIMO ")
else:
    print(f"{numero} NO ES PRIMO")