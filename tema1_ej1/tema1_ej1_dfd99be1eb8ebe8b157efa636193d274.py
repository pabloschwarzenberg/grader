s=0
for i in range(n+1):
s+=i
p=1
s1=str(s)
for numero in s1:
if numero=="0":
      continue
p*=int(numero)
print("La suma de 1 hasta",n,"es",s)
print("El producto de sus digitos distintos de 0 es",p)